#!/usr/bin/env python3
"""Report and optionally convert Obsidian links into GitHub Pages-friendly links."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit


IMAGE_SUFFIXES = {
    ".avif",
    ".bmp",
    ".gif",
    ".ico",
    ".jpeg",
    ".jpg",
    ".png",
    ".svg",
    ".tif",
    ".tiff",
    ".webp",
}
LINK_SUFFIXES = IMAGE_SUFFIXES | {".md"}
WIKI_LINK_RE = re.compile(r"(!?)\[\[([^\]\n]+)\]\]")
MARKDOWN_LINK_RE = re.compile(r"(!?)\[([^\]\n]*)\]\((<[^>\n]+>|[^)\n]+)\)")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
EXTERNAL_SCHEMES = ("http", "https", "mailto", "tel", "data", "ftp", "obsidian")


def normalize(value: str) -> str:
    return unicodedata.normalize("NFC", value).casefold().replace("\\", "/")


def split_alias(value: str) -> tuple[str, str | None]:
    separator = value.find("|")
    if separator < 0:
        return value.strip(), None
    target = value[:separator].removesuffix("\\").strip()
    alias = value[separator + 1 :].strip().replace(r"\|", "|")
    return target, alias


def split_fragment(target: str) -> tuple[str, str]:
    path, separator, fragment = target.partition("#")
    return path.strip(), f"#{fragment}" if separator else ""


def relative_url(source: Path, target: Path, fragment: str) -> str:
    relative = os.path.relpath(target, start=source.parent).replace("\\", "/")
    if not relative.startswith("."):
        relative = f"./{relative}"
    return quote(relative, safe="/-._~'") + quote(fragment, safe="#-._~'") if fragment else quote(
        relative, safe="/-._~'"
    )


class Vault:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.files = {
            path.resolve()
            for path in self.root.rglob("*")
            if path.is_file() and path.suffix.casefold() in LINK_SUFFIXES
        }
        self.by_name: dict[str, list[Path]] = defaultdict(list)
        self.by_path: dict[str, Path] = {}
        for path in self.files:
            relative = path.relative_to(self.root).as_posix()
            self.by_name[normalize(path.name)].append(path)
            self.by_name[normalize(path.stem)].append(path)
            self.by_path[normalize(relative)] = path
            if path.suffix.casefold() == ".md":
                self.by_path[normalize(relative[:-3])] = path

    def resolve(self, source: Path, raw_target: str) -> tuple[Path | None, str]:
        target, fragment = split_fragment(unquote(raw_target).replace("\\", "/"))
        if not target:
            return source.resolve(), fragment

        target_path = Path(target)
        suffix = target_path.suffix.casefold()
        if suffix not in LINK_SUFFIXES:
            if not suffix:
                suffix = ".md"
            else:
                return None, fragment

        candidates: list[Path] = []

        if target.startswith("/"):
            root_candidate = (self.root / target.lstrip("/")).resolve()
            candidates.append(root_candidate if root_candidate.suffix else Path(f"{root_candidate}{suffix}"))
        else:
            source_candidate = (source.parent / target).resolve()
            candidates.append(source_candidate if source_candidate.suffix else Path(f"{source_candidate}{suffix}"))

            root_candidate = (self.root / target).resolve()
            if root_candidate not in candidates:
                candidates.append(root_candidate if root_candidate.suffix else Path(f"{root_candidate}{suffix}"))

        for candidate in candidates:
            try:
                indexed_path = candidate.relative_to(self.root).as_posix()
            except ValueError:
                continue
            resolved = self.by_path.get(normalize(indexed_path))
            if resolved is not None:
                return resolved, fragment

        normalized_target = normalize(target)
        if "/" in normalized_target or suffix in IMAGE_SUFFIXES:
            possible = [
                path
                for path in self.files
                if normalize(path.relative_to(self.root).as_posix()).endswith(normalized_target)
                or (
                    suffix == ".md"
                    and normalize(path.relative_to(self.root).as_posix()).endswith(
                        f"{normalized_target}.md"
                    )
                )
            ]
            if not possible:
                lookup_name = target_path.name if target_path.suffix else f"{target_path.name}.md"
                possible = self.by_name.get(normalize(lookup_name), [])
        else:
            lookup_name = target_path.name if target_path.suffix else f"{target_path.name}.md"
            possible = self.by_name.get(normalize(lookup_name), [])

        unique = list(dict.fromkeys(possible))
        if len(unique) == 1:
            return unique[0], fragment
        if len(unique) > 1:
            return None, fragment
        return None, fragment


def masked_inline_code(line: str) -> list[bool]:
    masked = [False] * len(line)
    ticks = list(re.finditer(r"`+", line))
    index = 0
    while index < len(ticks):
        opener = ticks[index]
        closer = next(
            (item for item in ticks[index + 1 :] if len(item.group()) == len(opener.group())),
            None,
        )
        if closer is None:
            index += 1
            continue
        for position in range(opener.start(), closer.end()):
            masked[position] = True
        while index < len(ticks) and ticks[index].end() <= closer.end():
            index += 1
    return masked


def process_text(source: Path, text: str, vault: Vault) -> tuple[str, list[dict[str, object]]]:
    changes: list[dict[str, object]] = []
    output_lines: list[str] = []
    in_fence: str | None = None

    for line_number, original_line in enumerate(text.splitlines(keepends=True), start=1):
        fence = FENCE_RE.match(original_line)
        if fence:
            marker = fence.group(1)[0]
            if in_fence is None:
                in_fence = marker
            elif in_fence == marker:
                in_fence = None
            output_lines.append(original_line)
            continue
        if in_fence is not None:
            output_lines.append(original_line)
            continue

        masked = masked_inline_code(original_line)
        replacements: list[tuple[int, int, str]] = []

        def add_replacement(
            match: re.Match[str],
            raw_target: str,
            replacement_label: str,
            is_embed: bool,
        ) -> None:
            if any(masked[match.start() : match.end()]):
                return
            target, fragment = vault.resolve(source, raw_target)
            if target is None:
                changes.append(
                    {
                        "file": source.relative_to(vault.root).as_posix(),
                        "line": line_number,
                        "old": match.group(0),
                        "status": "unresolved",
                    }
                )
                return
            url = relative_url(source, target, fragment)
            replacement = f"{'!' if is_embed else ''}[{replacement_label}]({url})"
            replacements.append((match.start(), match.end(), replacement))
            if replacement != match.group(0):
                changes.append(
                    {
                        "file": source.relative_to(vault.root).as_posix(),
                        "line": line_number,
                        "old": match.group(0),
                        "new": replacement,
                        "status": "changed",
                    }
                )

        for match in WIKI_LINK_RE.finditer(original_line):
            raw_target, alias = split_alias(match.group(2))
            is_embed = bool(match.group(1))
            if is_embed and alias and re.fullmatch(r"\d+(?:x\d+)?", alias, re.IGNORECASE):
                alias = None
            label = alias or Path(split_fragment(raw_target)[0]).stem or split_fragment(raw_target)[0]
            add_replacement(match, raw_target, label, is_embed)

        wiki_spans = [(match.start(), match.end()) for match in WIKI_LINK_RE.finditer(original_line)]
        for match in MARKDOWN_LINK_RE.finditer(original_line):
            if any(start <= match.start() < end for start, end in wiki_spans):
                continue
            destination = match.group(3)
            raw_target = destination[1:-1] if destination.startswith("<") else destination
            parsed = urlsplit(raw_target)
            if parsed.scheme.casefold() in EXTERNAL_SCHEMES or raw_target.startswith(("#", "//")):
                continue
            if " " in raw_target and not raw_target.startswith("<"):
                raw_target = raw_target.split(" ", 1)[0].strip()
            add_replacement(
                match,
                parsed.path + (f"#{parsed.fragment}" if parsed.fragment else ""),
                match.group(2),
                bool(match.group(1)),
            )

        for start, end, replacement in sorted(replacements, reverse=True):
            original_line = original_line[:start] + replacement + original_line[end:]
        output_lines.append(original_line)

    return "".join(output_lines), changes


def write_text_preserving_newlines(path: Path, content: str) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        stream.write(content)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Converti i collegamenti Obsidian del vault in collegamenti Markdown relativi."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Radice del vault da analizzare (predefinita: cartella docs).",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Applica le modifiche. Senza questa opzione viene eseguita una dry-run.",
    )
    parser.add_argument(
        "--json",
        type=Path,
        help="Scrive il report completo in un file JSON.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Mostra solo il riepilogo finale.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print(f"Errore: cartella non trovata: {root}", file=sys.stderr)
        return 2

    vault = Vault(root)
    all_changes: list[dict[str, object]] = []
    modified_files = 0

    for source in sorted(root.rglob("*.md"), key=lambda path: normalize(path.as_posix())):
        text = source.read_text(encoding="utf-8")
        converted, changes = process_text(source, text, vault)
        all_changes.extend(changes)
        if converted != text and args.write:
            write_text_preserving_newlines(source, converted)
            modified_files += 1

    changed = [change for change in all_changes if change["status"] == "changed"]
    unresolved = [change for change in all_changes if change["status"] == "unresolved"]

    if not args.quiet:
        for change in changed:
            print(f'{change["file"]}:{change["line"]}: {change["old"]} -> {change["new"]}')
        for change in unresolved:
            print(f'{change["file"]}:{change["line"]}: NON RISOLTO: {change["old"]}', file=sys.stderr)

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(
            json.dumps(all_changes, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    action = "Applicati" if args.write else "Da convertire"
    print(
        f"{action}: {len(changed)} collegamenti; non risolti: {len(unresolved)}; "
        f"file modificabili: {len({change['file'] for change in changed})}; "
        f"file modificati: {modified_files}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

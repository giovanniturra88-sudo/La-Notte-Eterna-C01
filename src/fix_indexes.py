from pathlib import Path
import re

INDEX_FILES = {
    "Meteore",
    "Divinità",
    "Background",
    "Domini delle Classi",
    "SottoClassi",
}

updated = 0

for md in Path(".").rglob("*.md"):

    if md.stem not in INDEX_FILES:
        continue

    text = md.read_text(
        encoding="utf-8"
    )

    new_text = re.sub(
        r"(?m)^type:\s*.+?$",
        "type: Indice",
        text
    )

    if new_text != text:

        md.write_text(
            new_text,
            encoding="utf-8"
        )

        updated += 1

        print(
            f"{md.stem} -> Indice"
        )

print()
print(
    f"Aggiornati {updated} file"
)
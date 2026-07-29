from pathlib import Path
import re

ROOT = Path(".")

TYPE_MAP = {
    "domain": "Dominio",
    "environment": "Scenario",
}

updated = 0

for md in ROOT.rglob("*.md"):

    try:
        text = md.read_text(
            encoding="utf-8"
        )
    except Exception:
        continue

    if not text.startswith("---"):
        continue

    m = re.search(
        r"(?m)^type:\s*(.+?)\s*$",
        text
    )

    if not m:
        continue

    old_type = m.group(1).strip()

    if old_type not in TYPE_MAP:
        continue

    new_type = TYPE_MAP[old_type]

    new_text = re.sub(
        r"(?m)^type:\s*.+?$",
        f"type: {new_type}",
        text,
        count=1
    )

    md.write_text(
        new_text,
        encoding="utf-8"
    )

    updated += 1

    print(
        f"✓ {md.name}: "
        f"{old_type} -> {new_type}"
    )

print()
print(f"Aggiornati: {updated}")

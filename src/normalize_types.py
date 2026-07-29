from pathlib import Path
import re

ROOT = Path(".")

TYPE_MAP = {
    "npc": "PNG",
    "location": "Luogo",
    "ancestry": "Popolo",
    "divinita": "Divinità",
    "artifact": "Artefatto",
    "lore": "Lore",

    "class": "Classe",
    "subclass": "Sottoclasse",
    "ability": "Abilità",

    "weapon": "Equipaggiamento",
    "armor": "Equipaggiamento",

    "item": "Oggetto",
    "consumable": "Oggetto",

    "enemy": "Creatura",
    "beast_form": "Creatura",

    "house_rule": "Regola",
}

updated = 0
skipped = 0

for md in ROOT.rglob("*.md"):

    try:
        text = md.read_text(encoding="utf-8")
    except Exception:
        continue

    if not text.startswith("---"):
        continue

    match = re.search(
        r"(?m)^type:\s*(.+?)\s*$",
        text
    )

    if not match:
        continue

    old_type = match.group(1).strip()

    if old_type not in TYPE_MAP:
        skipped += 1
        continue

    new_type = TYPE_MAP[old_type]

    new_text = re.sub(
        r"(?m)^type:\s*.+?$",
        f"type: {new_type}",
        text,
        count=1
    )

    if new_text != text:

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
print(f"Saltati:    {skipped}")

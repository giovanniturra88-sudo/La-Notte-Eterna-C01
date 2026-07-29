from pathlib import Path
import re

TYPE_BY_NAME = {
    "Benvenuto": "Indice",
    "Home": "Indice",
    "Indice Artefatti": "Indice",
    "Indice Luoghi": "Indice",
    "Indice NPC": "Indice",
    "Template Ancestry": "Template",
    "Transformations": "Regola",
}

updated = 0

for md in Path(".").rglob("*.md"):

    if md.stem not in TYPE_BY_NAME:
        continue

    try:
        text = md.read_text(encoding="utf-8")
    except:
        continue

    new_type = TYPE_BY_NAME[md.stem]

    if re.search(r"(?m)^type:\s*", text):

        new_text = re.sub(
            r"(?m)^type:\s*.+?$",
            f"type: {new_type}",
            text,
            count=1
        )

    elif text.startswith("---"):
        new_text = text.replace(
            "---",
            f"---\ntype: {new_type}",
            1
        )

    else:
        new_text = (
            f"---\n"
            f"type: {new_type}\n"
            f"---\n\n"
            f"{text}"
        )

    if new_text != text:

        md.write_text(
            new_text,
            encoding="utf-8"
        )

        updated += 1

        print(
            f"{md.stem} -> {new_type}"
        )

print()
print(f"Aggiornati {updated} file")
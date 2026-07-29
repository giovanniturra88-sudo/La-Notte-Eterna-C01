from pathlib import Path
import re

updated = 0

for md in Path(".").rglob("*.md"):

    try:
        text = md.read_text(
            encoding="utf-8"
        )
    except:
        continue

    new_text = re.sub(
        r"(?m)^type:\s*community\s*$",
        "type: Background",
        text
    )

    if new_text != text:

        md.write_text(
            new_text,
            encoding="utf-8"
        )

        updated += 1

        print(md.stem)

print()
print(f"Aggiornati {updated} file")
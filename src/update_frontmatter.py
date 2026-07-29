from pathlib import Path
import re

ROOT = Path(".")

for md in ROOT.rglob("*.md"):

    try:
        text = md.read_text(
            encoding="utf-8"
        )
    except:
        continue

    if not text.startswith("---"):
        continue

    text2 = re.sub(
        r"type:\s*deity_or_faction",
        "type: divinita",
        text
    )

    if text2 != text:

        md.write_text(
            text2,
            encoding="utf-8"
        )

        print(
            f"Aggiornato: {md.name}"
        )
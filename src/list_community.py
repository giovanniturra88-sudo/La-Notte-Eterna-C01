# list_community.py

from pathlib import Path
import re

for md in Path(".").rglob("*.md"):

    try:
        text = md.read_text(
            encoding="utf-8"
        )
    except:
        continue

    m = re.search(
        r"(?m)^type:\s*(.+?)\s*$",
        text
    )

    if m and m.group(1).strip() == "community":
        print(md.stem)
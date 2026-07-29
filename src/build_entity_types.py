import csv
import re
from pathlib import Path

ROOT = Path(".")

rows = []

for md in ROOT.rglob("*.md"):

    try:
        text = md.read_text(
            encoding="utf-8"
        )
    except Exception:
        continue

    file_type = "unknown"

    if text.startswith("---"):

        m = re.search(
            r"(?m)^type:\s*(.+?)\s*$",
            text
        )

        if m:
            file_type = m.group(1).strip()

    rows.append({
        "name": md.stem,
        "type": file_type
    })

rows.sort(
    key=lambda x: (
        x["type"],
        x["name"]
    )
)

with open(
    "entity_types.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.DictWriter(
        f,
        fieldnames=[
            "name",
            "type"
        ]
    )

    writer.writeheader()
    writer.writerows(rows)

print(
    f"Generate {len(rows)} entità"
)
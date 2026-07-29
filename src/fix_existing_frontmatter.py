import csv
from pathlib import Path

catalog = {}

with open("vault_catalog.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row["type"] != "unknown":
            catalog[row["path"]] = row["type"]

for rel_path, file_type in catalog.items():

    path = Path(rel_path)

    if not path.exists():
        continue

    text = path.read_text(encoding="utf-8")

    if not text.startswith("---"):
        continue

    lines = text.splitlines()

    # trova la fine del frontmatter
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break

    if end is None:
        continue

    frontmatter = lines[:end+1]

    already_has_type = any(
        line.strip().startswith("type:")
        for line in frontmatter
    )

    if already_has_type:
        continue

    frontmatter.insert(1, f"type: {file_type}")

    new_text = "\n".join(frontmatter)
    new_text += "\n" + "\n".join(lines[end+1:])

    path.write_text(new_text, encoding="utf-8")

    print("AGGIORNATO:", rel_path)

print("\nFatto.")
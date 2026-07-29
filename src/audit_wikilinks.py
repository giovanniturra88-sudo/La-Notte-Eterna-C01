from pathlib import Path
import csv
import re

entities = set()

with open("entity_types.csv", encoding="utf-8") as f:
    next(f)

    for line in f:
        name = line.split(",")[0].strip()
        entities.add(name)

found = []

for md in Path(".").rglob("*.md"):

    try:
        text = md.read_text(
            encoding="utf-8"
        )
    except:
        continue

    for entity in entities:

        if len(entity) < 5:
            continue

        if entity not in text:
            continue

        if f"[[{entity}]]" in text:
            continue

        found.append(
            (
                md.stem,
                entity
            )
        )

with open(
    "missing_wikilinks.csv",
    "w",
    encoding="utf-8"
) as f:

    f.write("source,entity\n")

    for source, entity in found:
        f.write(
            f'"{source}","{entity}"\n'
        )

print(
    f"Trovate {len(found)} possibili occorrenze"
)
import csv

entities = {}

with open(
    "vault_catalog.csv",
    encoding="utf-8"
) as f:

    reader = csv.DictReader(f)

    for row in reader:

        entities[
            row["name"].replace(".md", "")
        ] = row["type"]

with open(
    "entity_types.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:

    w = csv.writer(f)

    w.writerow([
        "name",
        "type"
    ])

    for k, v in sorted(
        entities.items()
    ):

        w.writerow([k, v])

print(
    f"Create {len(entities)} entità"
)
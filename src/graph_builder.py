import csv

types = {}

with open(
    "entity_types.csv",
    encoding="utf-8"
) as f:

    r = csv.DictReader(f)

    for row in r:
        types[row["name"]] = row["type"]

edges = []

with open(
    "vault_links.csv",
    encoding="utf-8"
) as f:

    r = csv.DictReader(f)

    for row in r:

        edges.append({

            "source":
                row["source"],

            "source_type":
                types.get(
                    row["source"],
                    "unknown"
                ),

            "target":
                row["target"],

            "target_type":
                types.get(
                    row["target"],
                    "unknown"
                ),

            "relationship":
                "references"
        })

with open(
    "knowledge_graph.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:

    w = csv.DictWriter(
        f,
        fieldnames=[
            "source",
            "source_type",
            "target",
            "target_type",
            "relationship"
        ]
    )

    w.writeheader()
    w.writerows(edges)

print(
    f"Creati {len(edges)} archi"
)
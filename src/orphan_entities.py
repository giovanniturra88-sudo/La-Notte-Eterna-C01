import csv
from collections import Counter

links = Counter()

with open("knowledge_graph_clean.csv", encoding="utf-8") as f:

    reader = csv.DictReader(f)

    for row in reader:

        links[row["source"]] += 1
        links[row["target"]] += 1

with open("entity_types.csv", encoding="utf-8") as f:

    reader = csv.DictReader(f)

    print("\n=== ENTITA ORFANE ===\n")

    for row in reader:

        if links[row["name"]] == 0:

            print(
                row["type"],
                "-",
                row["name"]
            )
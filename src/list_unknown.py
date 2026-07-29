# list_unknown.py

import csv

with open("entity_types.csv", encoding="utf-8") as f:
    r = csv.DictReader(f)

    print("\n=== UNKNOWN ===\n")

    for row in r:
        if row["type"] == "unknown":
            print(row["name"])
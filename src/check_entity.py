import csv
from collections import Counter

c = Counter()

with open("entity_types.csv", encoding="utf-8") as f:
    r = csv.DictReader(f)

    for row in r:
        c[row["type"]] += 1

for k, v in sorted(c.items()):
    print(f"{k}: {v}")
import csv

for t in ["Classe", "Sottoclasse", "Background", "Scenario"]:
    print("\n" + "=" * 50)
    print(t)
    print("=" * 50)

    with open("entity_types.csv", encoding="utf-8") as f:
        r = csv.DictReader(f)

        for row in r:
            if row["type"] == t:
                print(row["name"])
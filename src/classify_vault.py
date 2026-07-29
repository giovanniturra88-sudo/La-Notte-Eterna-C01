from pathlib import Path
from collections import Counter

rules = {
    r"03_Campagna\PNG": "npc",
    r"01_Lore\Geografia": "location",
    r"01_Lore\Divinità_e_Fazioni": "deity_or_faction",
    r"02_Meccaniche_DaggerHeart\Nemici": "enemy",
    r"02_Meccaniche_DaggerHeart\Classi": "class",
    r"02_Meccaniche_DaggerHeart\SottoClassi": "subclass",
    r"02_Meccaniche_DaggerHeart\Armi": "weapon",
    r"02_Meccaniche_DaggerHeart\Armature": "armor",
    r"02_Meccaniche_DaggerHeart\Consumabili": "consumable",
    r"02_Meccaniche_DaggerHeart\Domini": "domain",
}

counter = Counter()

for md in Path(".").rglob("*.md"):
    rel = str(md)

    category = "unknown"

    for rule, value in rules.items():
        if rule in rel:
            category = value
            break

    counter[category] += 1

print("\n=== CLASSIFICAZIONE VAULT ===\n")

for k, v in sorted(counter.items()):
    print(f"{k:20} {v}")

print("\nTotale:", sum(counter.values()))
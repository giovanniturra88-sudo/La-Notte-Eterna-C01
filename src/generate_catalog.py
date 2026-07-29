from pathlib import Path
import csv

rules = {
    r"03_Campagna\PNG": "npc",
    r"01_Lore\Geografia": "location",
    r"01_Lore\Divinità_e_Fazioni": "deity_or_faction",
    r"01_Lore\Cosmologia\Meteore": "artifact",
    r"01_Lore\Cosmologia": "lore",
    r"01_Lore\Razze_e_Popoli": "ancestry",
    r"01_Lore\Vera Magia": "lore",

    r"02_Meccaniche_DaggerHeart\Abilità": "ability",
    r"02_Meccaniche_DaggerHeart\Ambienti": "environment",
    r"02_Meccaniche_DaggerHeart\Ancestry_e_Community\Ancestry": "ancestry",
    r"02_Meccaniche_DaggerHeart\Comunità": "community",
    r"02_Meccaniche_DaggerHeart\Forme Bestiali": "beast_form",
    r"02_Meccaniche_DaggerHeart\items": "item",

    r"02_Meccaniche_DaggerHeart\Nemici": "enemy",
    r"02_Meccaniche_DaggerHeart\Classi": "class",
    r"02_Meccaniche_DaggerHeart\SottoClassi": "subclass",
    r"02_Meccaniche_DaggerHeart\Armi": "weapon",
    r"02_Meccaniche_DaggerHeart\Armature": "armor",
    r"02_Meccaniche_DaggerHeart\Consumabili": "consumable",
    r"02_Meccaniche_DaggerHeart\Domini": "domain",
    r"02_Meccaniche_DaggerHeart\Regole_di_Casa": "house_rule",
}

rows = []

for md in Path(".").rglob("*.md"):

    rel = str(md)

    category = "unknown"

    for rule, value in rules.items():
        if rule in rel:
            category = value
            break

    rows.append([
        md.name,
        rel,
        category
    ])

with open("vault_catalog.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "path", "type"])
    writer.writerows(rows)

print(f"Creato vault_catalog.csv con {len(rows)} record")
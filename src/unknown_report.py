from pathlib import Path

rules = [
    r"03_Campagna\PNG",
    r"01_Lore\Geografia",
    r"01_Lore\Divinità_e_Fazioni",
    r"02_Meccaniche_DaggerHeart\Nemici",
    r"02_Meccaniche_DaggerHeart\Classi",
    r"02_Meccaniche_DaggerHeart\SottoClassi",
    r"02_Meccaniche_DaggerHeart\Armi",
    r"02_Meccaniche_DaggerHeart\Armature",
    r"02_Meccaniche_DaggerHeart\Consumabili",
    r"02_Meccaniche_DaggerHeart\Domini",
]

with open("unknown_files.txt", "w", encoding="utf-8") as f:

    for md in Path(".").rglob("*.md"):

        rel = str(md)

        matched = False

        for rule in rules:
            if rule in rel:
                matched = True
                break

        if not matched:
            f.write(rel + "\n")

print("Creato unknown_files.txt")

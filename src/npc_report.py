from pathlib import Path

for md in Path("03_Campagna/PNG").glob("*.md"):
    print(md.stem)
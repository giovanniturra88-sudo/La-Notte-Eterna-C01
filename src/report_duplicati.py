from pathlib import Path
from collections import defaultdict

names = defaultdict(list)

for md in Path(".").rglob("*.md"):
    names[md.stem.lower()].append(md.stem)

for key, values in sorted(names.items()):

    unique = sorted(set(values))

    if len(unique) > 1:
        print()
        print("Possibile duplicato:")
        print(unique)
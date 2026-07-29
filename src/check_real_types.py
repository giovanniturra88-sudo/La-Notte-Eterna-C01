from pathlib import Path
import re
from collections import Counter

c = Counter()

for md in Path(".").rglob("*.md"):

    try:
        text = md.read_text(encoding="utf-8")
    except:
        continue

    m = re.search(
        r"(?m)^type:\s*(.+?)\s*$",
        text
    )

    if m:
        c[m.group(1).strip()] += 1

print()

for k, v in sorted(c.items()):
    print(f"{k}: {v}")
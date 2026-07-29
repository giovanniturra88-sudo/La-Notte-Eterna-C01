from pathlib import Path
import re

suspects = [
    "Background",
    "Divinità",
    "Domini delle Classi",
    "SottoClassi",
    "Meteore"
]

for md in Path(".").rglob("*.md"):

    if md.stem in suspects:

        print("\n" + "=" * 60)
        print(md.stem)
        print(md)

        txt = md.read_text(
            encoding="utf-8"
        )

        m = re.search(
            r"(?m)^type:\s*(.+?)\s*$",
            txt
        )

        if m:
            print("TYPE =", m.group(1))
import re
import csv
from pathlib import Path

LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")

edges = []

for md in Path(".").rglob("*.md"):

    source = md.stem

    try:
        text = md.read_text(
            encoding="utf-8"
        )
    except:
        continue

    for match in LINK_RE.findall(text):

        target = match.split("|")[0].strip()

        edges.append({
            "source": source,
            "target": target,
            "relationship": "wiki_link"
        })

with open(
    "vault_links.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.DictWriter(
        f,
        fieldnames=[
            "source",
            "target",
            "relationship"
        ]
    )

    writer.writeheader()
    writer.writerows(edges)

print(
    f"Creati {len(edges)} collegamenti"
)
import csv
import re
from collections import Counter

INPUT = "knowledge_graph.csv"
OUTPUT = "knowledge_graph_clean.csv"

IMAGE_PATTERNS = [
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    "Pasted image"
]

ALIASES = {
    "urakian": "Urakian",
    "karevi": "Karevi",
    "wiloi": "Wiloi",
    "elfi": "Elfi",
    "nani": "Nani",
    "orchi": "Orchi",
    "giganti": "Giganti",
    "hjilaki": "Hjilaki",
}

def normalize(name):

    if not name:
        return name

    n = name.strip()

    if n in ALIASES:
        return ALIASES[n]

    return n

def is_image(value):

    value = value.lower()

    return any(
        x.lower() in value
        for x in IMAGE_PATTERNS
    )

counter = Counter()
types = {}

with open(
    INPUT,
    encoding="utf-8"
) as f:

    reader = csv.DictReader(f)

    for row in reader:

        source = normalize(
            row["source"]
        )

        target = normalize(
            row["target"]
        )

        # elimina immagini
        if is_image(source):
            continue

        if is_image(target):
            continue

        # elimina self-link
        if source == target:
            continue

        key = (
            source,
            row["source_type"],
            target,
            row["target_type"]
        )

        counter[key] += 1

with open(
    OUTPUT,
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.writer(f)

    writer.writerow([
        "source",
        "source_type",
        "target",
        "target_type",
        "weight"
    ])

    for (
        source,
        source_type,
        target,
        target_type
    ), weight in sorted(
        counter.items(),
        key=lambda x: x[1],
        reverse=True
    ):

        writer.writerow([
            source,
            source_type,
            target,
            target_type,
            weight
        ])

print(
    f"Creati {len(counter)} archi puliti"
)
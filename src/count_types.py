from pathlib import Path
from collections import Counter

counter = Counter()

for md in Path(".").rglob("*.md"):

    try:
        text = md.read_text(encoding="utf-8")

        if text.startswith("---"):
            lines = text.splitlines()

            for line in lines:
                if line.startswith("type:"):
                    t = line.split(":", 1)[1].strip()
                    counter[t] += 1
                    break

    except Exception as e:
        print(f"Errore: {md} -> {e}")

print("\n=== TIPI PRESENTI ===\n")

for k, v in sorted(counter.items()):
    print(f"{k:20} {v}")

print("\nTotale:", sum(counter.values()))
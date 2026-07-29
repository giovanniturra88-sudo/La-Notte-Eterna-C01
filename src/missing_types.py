from pathlib import Path

missing = []

for md in Path(".").rglob("*.md"):
    try:
        text = md.read_text(encoding="utf-8")

        if "type:" not in text[:500]:
            missing.append(str(md))

    except Exception as e:
        print(e)

print("Mancanti:", len(missing))

with open("missing_types.txt", "w", encoding="utf-8") as f:
    for x in missing:
        f.write(x + "\n")
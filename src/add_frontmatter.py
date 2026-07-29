import csv
from pathlib import Path

with open("vault_catalog.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:

        file_path = Path(row["path"])
        file_type = row["type"]

        # Salta i file non classificati
        if file_type == "unknown":
            continue

        if not file_path.exists():
            print(f"NON TROVATO: {file_path}")
            continue

        content = file_path.read_text(encoding="utf-8")

        # Se ha già un frontmatter, salta
        if content.lstrip().startswith("---"):
            print(f"GIÀ OK: {file_path}")
            continue

        frontmatter = f"---\ntype: {file_type}\n---\n\n"

        file_path.write_text(
            frontmatter + content,
            encoding="utf-8"
        )

        print(f"AGGIORNATO: {file_path}")

print("\nFatto.")

from pathlib import Path

CURRENT = Path(r".")
BACKUP = Path(r"..\La Notte Eterna C01 IT")  # modifica il percorso

current_files = {
    str(p.relative_to(CURRENT)).lower()
    for p in CURRENT.rglob("*.md")
}

backup_files = {
    str(p.relative_to(BACKUP)).lower()
    for p in BACKUP.rglob("*.md")
}

missing_in_current = sorted(
    backup_files - current_files
)

new_in_current = sorted(
    current_files - backup_files
)

print("\n===== MANCANTI NELLA VAULT ATTUALE =====\n")

for f in missing_in_current:
    print(f)

print(
    f"\nTotale mancanti: {len(missing_in_current)}"
)

print("\n===== NUOVI NELLA VAULT ATTUALE =====\n")

for f in new_in_current:
    print(f)

print(
    f"\nTotale nuovi: {len(new_in_current)}"
)
import os
import re
import yaml

def fix_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines or not lines[0].startswith('---'):
        return False  # Non ha un frontmatter

    # Isola il blocco Frontmatter fino all'ultimo '---' prima del contenuto vero
    frontmatter_lines = []
    body_lines = []
    in_frontmatter = False
    header_count = 0

    for i, line in enumerate(lines):
        if line.strip() == '---':
            header_count += 1
            if header_count == 1:
                in_frontmatter = True
                continue
            # Se siamo nel frontmatter e la riga successiva NON è una chiave YAML o un nuovo '---',
            # potrebbe essere l'inizio del corpo markdown.
            if i + 1 < len(lines) and (lines[i+1].startswith('#') or lines[i+1].strip() == ''):
                in_frontmatter = False
                body_lines = lines[i+1:]
                break
        
        if in_frontmatter:
            frontmatter_lines.append(line)
        else:
            body_lines.append(line)

    # Estrai le chiavi uniche mantenendo la prima occorrenza
    seen_keys = set()
    cleaned_yaml_lines = []

    for line in frontmatter_lines:
        match = re.match(r'^\s*([a-zA-Z0-9_-]+)\s*:', line)
        if match:
            key = match.group(1).lower()
            if key in seen_keys:
                continue  # Salta se già vista
            seen_keys.add(key)
        cleaned_yaml_lines.append(line)

    # Costruisci il nuovo contenuto
    new_frontmatter = "".join(cleaned_yaml_lines).strip()
    new_body = "".join(body_lines)

    new_content = f"---\n{new_frontmatter}\n---\n\n{new_body.lstrip()}"

    # Sovrascrivi il file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def process_directory(folder_path):
    updated = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                try:
                    if fix_file(path):
                        print(f"Pulito: {file}")
                        updated += 1
                except Exception as e:
                    print(f"Errore su {file}: {e}")

    print(f"\nOperazione completata! Modificati {updated} file.")

if __name__ == "__main__":
    folder = input("Incolla il percorso della cartella: ").strip().strip('"\'')
    if os.path.exists(folder):
        process_directory(folder)
    else:
        print("Percorso non trovato.")
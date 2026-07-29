import os
import re
import json

def load_transcoding_table(json_path='transcoding_table.json'):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('detailed_mapping', {})

def transform_value(key, value, mapping):
    """
    Mappa il valore corrente usando la tabella di transcodifica.
    Gestisce anche le stringhe racchiuse tra virgolette o prive di esse.
    """
    if key not in mapping:
        return value

    key_map = mapping[key]
    clean_val = value.strip().strip('"\'')

    # Cerca riscontro sia col valore grezzo che col valore tra virgolette
    if clean_val in key_map:
        new_val = key_map[clean_val]
    elif f'"{clean_val}"' in key_map:
        new_val = key_map[f'"{clean_val}"']
    elif value.strip() in key_map:
        new_val = key_map[value.strip()]
    else:
        return value  # Se non presente nella mappa, mantiene il valore originale

    # Se il valore mappato ha virgolette nello JSON, lo ripuliamo per coerenza
    return new_val.strip('"\'')

def process_file(file_path, mapping):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Isolamento Frontmatter YAML e Corpo
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)
    
    if not match:
        return False

    frontmatter_raw = match.group(1)
    body = match.group(2)

    # 2. Transcodifica e de-duplicazione del Frontmatter
    seen_keys = set()
    cleaned_yaml_lines = []

    for line in frontmatter_raw.splitlines():
        key_match = re.match(r'^\s*([a-zA-Z0-9_-]+)\s*:\s*(.*)$', line)
        if key_match:
            key = key_match.group(1).lower()
            val = key_match.group(2).strip()

            if key in seen_keys:
                continue  # Rimuove duplicati mantenendo il primo
            seen_keys.add(key)

            # Transcodifica il valore
            new_val = transform_value(key, val, mapping)
            
            # Se contiene spazi o caratteri speciali, mantieni le virgolette
            if " " in new_val and not (new_val.startswith("[") or new_val.startswith('"')):
                new_val = f'"{new_val}"'

            cleaned_yaml_lines.append(f"{key_match.group(1)}: {new_val}")
        else:
            cleaned_yaml_lines.append(line)

    # 3. Rimozione della sezione ### STATISTICHE dal corpo
    # Rimuove '### STATISTICHE' e le righe con elenchi puntati subito successive
    body_cleaned = re.sub(
        r'###\s*STATISTICHE\s*\n(\s*\*.*?\n)*', 
        '', 
        body, 
        flags=re.IGNORECASE
    ).strip()

    # 4. Ricostruzione del file
    new_frontmatter = "\n".join(cleaned_yaml_lines)
    new_content = f"---\n{new_frontmatter}\n---\n\n{body_cleaned}\n"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def process_folder(folder_path, json_path):
    mapping = load_transcoding_table(json_path)
    count = 0

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                try:
                    if process_file(full_path, mapping):
                        count += 1
                        print(f"Aggiornato: {file}")
                except Exception as e:
                    print(f"Errore su {file}: {e}")

    print(f"\nOperazione completata! Modificati {count} file.")

if __name__ == "__main__":
    folder = input("Inserisci il percorso della cartella Markdown: ").strip().strip('"\'')
    json_file = input("Inserisci il percorso di transcoding_table.json (invio per locale): ").strip().strip('"\'')
    
    if not json_file:
        json_file = "transcoding_table.json"

    if os.path.exists(folder) and os.path.exists(json_file):
        process_folder(folder, json_file)
    else:
        print("Errore: Cartella o file JSON non trovato.")
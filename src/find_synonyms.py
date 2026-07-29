import os
import re
from collections import defaultdict

SOURCE_DIR = "02_Meccaniche_DaggerHeart/Armi_Daggerheart"

def analyze_values():
    values_by_field = {
        "INGOMBRO": defaultdict(set),
        "GITTATA / PORTATA": defaultdict(set),
        "TRATTO": defaultdict(set),
        "DANNO / TIPO DANNO": defaultdict(set),
        "BADGE HEADER (Livello/Grado/Ruolo/Ecc)": defaultdict(set)
    }

    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith('.md')]

    for filename in files:
        filepath = os.path.join(SOURCE_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Scansione Elenco Puntato (- **Chiave:** Valore)
        # Accetta qualsiasi formattazione per la chiave (con o senza asterischi, spazi, ecc.)
        list_matches = re.findall(r'^\s*[-*]\s*\*?\_?\*?([^:\n\r]+?)\*?\_?\*?\s*:\s*(.+)$', content, re.MULTILINE)
        
        for key, val in list_matches:
            clean_key = key.strip(" *_-\t").lower()
            clean_val = val.strip(" *_-\t")

            if "ingombro" in clean_key:
                values_by_field["INGOMBRO"][clean_val].add(filename)
            elif "gittata" in clean_key or "portata" in clean_key:
                values_by_field["GITTATA / PORTATA"][clean_val].add(filename)
            elif "tratto" in clean_key:
                values_by_field["TRATTO"][clean_val].add(filename)
            elif "danno" in clean_key:
                values_by_field["DANNO / TIPO DANNO"][clean_val].add(filename)

        # 2. Scansione Badge/Tag subito sotto il Titolo # (es: **_Livello 3_** _Secondario_ _Fisico_)
        # Prende tutte le parole racchiuse da corsivo o grassetto nelle prime 10 righe
        lines = content.splitlines()[:10]
        header_block = "\n".join(lines)
        
        badges = re.findall(r'[_*]{1,2}([^_*]+?)[_*]{1,2}', header_block)
        for badge in badges:
            clean_badge = badge.strip()
            # Escludiamo le chiavi dei bullet point già analizzate
            if clean_badge and not any(k in clean_badge.lower() for k in ["tratto", "portata", "gittata", "danno", "ingombro"]):
                values_by_field["BADGE HEADER (Livello/Grado/Ruolo/Ecc)"][clean_badge].add(filename)

    # STAMPA REPORT
    print("==================================================")
    print("📊 LISTA VALORI E SINONIMI TROVATI NEI FILE")
    print("==================================================\n")

    for field, val_dict in values_by_field.items():
        print(f"📁 VALORI TROVATI PER: [{field}]")
        print("-" * 50)
        if not val_dict:
            print("  (Nessun valore individuato)")
        for val, file_set in sorted(val_dict.items(), key=lambda x: len(x[1]), reverse=True):
            print(f"  • \"{val}\" ➔ presente in {len(file_set)} file")
        print()

if __name__ == "__main__":
    if os.path.exists(SOURCE_DIR):
        analyze_values()
    else:
        print(f"❌ Percorso non trovato: {SOURCE_DIR}")
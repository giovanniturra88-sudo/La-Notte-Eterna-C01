import os
import re

SOURCE_DIR = r"02_Meccaniche_DaggerHeart\Armi_IT"
OUTPUT_DIR = r"02_Meccaniche_DaggerHeart\Armi_Daggerheart"


def restructure_file(content, filename):
    # 1. Estrazione Frontmatter YAML originale
    orig_name_match = re.search(r'original_name:\s*["\']?(.*?)["\']?\n', content)
    alias_match = re.search(r'alias:\s*\[(.*?)\]', content)
    
    orig_name = orig_name_match.group(1) if orig_name_match else os.path.splitext(filename)[0]
    alias = alias_match.group(1) if alias_match else f'"{orig_name}"'

    # Titolo principale (# Titolo)
    title_match = re.search(r'^#\s+(.*)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else orig_name

    # 2. Estrazione Tier (intercetta: Tier, Fascia, Livello, Grado)
    tier_match = re.search(r'(?:Tier|Fascia|Livello|Grado)\s+(\d+)', content, re.IGNORECASE)
    tier_val = tier_match.group(1) if tier_match else "1"

    # Estrazione Ruolo ROBUSTA (cerca primari/a/o o secondari/a/o ovunque nel file)
    ruolo = "-"
    if re.search(r'secondari[ao]', content, re.IGNORECASE):
        ruolo = "Secondaria"
    elif re.search(r'primari[ao]', content, re.IGNORECASE):
        ruolo = "Primaria"

    # Estrazione Categoria
    categoria = "Arma" if re.search(r'\bArma\b', content, re.IGNORECASE) else ("Scudo" if re.search(r'\bScudo\b', content, re.IGNORECASE) else "Equipaggiamento")

    # 3. Estrazione Statistiche grezze
    tratto = re.search(r'-\s*\*\*Tratto:\*\*\s*(.*)', content, re.IGNORECASE)
    gittata = re.search(r'-\s*\*\*(?:Gittata|Portata):\*\*\s*(.*)', content, re.IGNORECASE)
    danno_raw = re.search(r'-\s*\*\*Danno:\*\*\s*(.*)', content, re.IGNORECASE)
    ingombro = re.search(r'-\s*\*\*Ingombro:\*\*\s*(.*)', content, re.IGNORECASE)

    tratto_val = tratto.group(1).strip() if tratto else "-"
    gittata_val = gittata.group(1).strip() if gittata else "-"
    danno_str = danno_raw.group(1).strip() if danno_raw else "-"
    ingombro_val = ingombro.group(1).strip() if ingombro else "-"

    # 4. Rilevazione Tipo Danno Robusta (con supporto phy/fis/mag)
    tipo_danno = "-"
    danno_lower = danno_str.lower()
    if re.search(r'\bMagic[ao]\b', content, re.IGNORECASE) or any(w in danno_lower for w in ["mag", "magi"]):
        tipo_danno = "Magica"
    elif re.search(r'\bFisic[ao]\b', content, re.IGNORECASE) or any(w in danno_lower for w in ["phy", "phys", "fis", "fisi"]):
        tipo_danno = "Fisica"

    # 5. Pulizia del campo Danno (rimuove il testo del tipo di danno lasciando la formula dei dadi)
    danno_clean = re.sub(r'\b(?:phy|phys|fis|fisi|mag|magi|fisico|magico)\b', '', danno_str, flags=re.IGNORECASE).strip()

    # 6. Estrazione RIGOROSA della sezione EFFETTO (e sinonimi)
    effetto_section = ""
    effetto_match = re.search(
        r'###\s*(?:EFFETTO|EFFETTI|TRATTO|TRATTI|CARATTERISTICA|CARATTERISTICHE|PROPRIETÀ|SPECIAL)\s*\n+([\s\S]*?)(?=\n---|\n#|$)', 
        content, 
        re.IGNORECASE
    )
    if effetto_match:
        effetto_body = effetto_match.group(1).strip()
        if effetto_body:
            effetto_section = f"---\n\n### EFFETTO\n\n{effetto_body}\n"

    # 7. Costruzione della scheda finale uniformata
    new_content = f"""---
type: Equipaggiamento
original_name: "{orig_name}"
alias: [{alias}]
categoria: {categoria}
tier: {tier_val}
ruolo: {ruolo}
tipo_danno: {tipo_danno}
tratto: {tratto_val}
gittata: {gittata_val}
danno: "{danno_clean}"
ingombro: "{ingombro_val}"
---

# {title}

> **{categoria} ({ruolo})** • **Tier:** {tier_val} • **Tipo:** {tipo_danno}

---

### STATISTICHE
* **Tratto:** {tratto_val}
* **Gittata:** {gittata_val}
* **Danno:** {danno_clean}
* **Ingombro:** {ingombro_val}

{effetto_section}"""
    return new_content.strip() + "\n"

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith('.md')]
    print(f"🧹 Ristrutturazione di {len(files)} file con estrazione corretta del RUOLO...")

    for filename in files:
        src_path = os.path.join(SOURCE_DIR, filename)
        dest_path = os.path.join(OUTPUT_DIR, filename)

        with open(src_path, 'r', encoding='utf-8') as f:
            content = f.read()

        new_file_content = restructure_file(content, filename)

        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(new_file_content)

    print(f"✅ Ristrutturazione completata con successo per tutti i {len(files)} file!")

if __name__ == "__main__":
    main()
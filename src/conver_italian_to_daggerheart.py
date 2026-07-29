import os
import re
import urllib.request
import json

# Cartella con i file già in Italiano da convertire
SOURCE_DIR = r"02_Meccaniche_DaggerHeart/Armi_IT"
OUTPUT_DIR = r"02_Meccaniche_DaggerHeart/Armi_Daggerheart"

SYSTEM_PROMPT = """
Sei un Game Designer esperto nella conversione di schede di gioco da D&D 5e a DAGGERHEART.
Ti viene fornita una scheda di un'arma in italiano. Il tuo compito è riconvertire esclusivamente la sezione delle statistiche e delle proprietà meccaniche secondo il regolamento di DAGGERHEART, lasciando inalterati i nomi, il testo narrativo e la struttura Obsidian.

REGOLAMENTO DAGGERHEART PER LE ARMI:
1. TIERS: Le armi vanno da Tier 0 (base/iniziale) a Tier 3 (leggendaria/incantata).
2. TRATTO PER L'ATTACCO: Scegli una tra [Agilità, Forza, Finesse, Istinto, Presenza, Sapienza] in base alla tipologia di arma.
3. GITTATA (RANGE): Scegli tra [Mischia, Molto Vicina, Vicina, Lontana, Molto Lontana].
4. DANNO: Esprimilo come combinazione di dado e tipo (es. d8 Fisico, d10 Magico). Converti i dadi di 5e mantenendo un valore equivalente.
5. MANI: [Una Mano] o [Due Mani].
6. TRATTI SPECIALI / CARATTERISTICHE:
   - Converti proprietà come 'Versatile', 'Accurata', 'Pesante' o bonus numerici (+1, +2) in Tratti di Daggerheart.
   - Usa la spesa di Speranza (es. "Spendi 1 Speranza per...") o il guadagno di Stress per attivare effetti speciali o danni extra.

FORMATO OUTPUT TASSATIVO:
Riconverti la scheda fornita rispettando la seguente struttura Markdown esatta:

---
system: Daggerheart
item_type: Weapon
original_name: "[Nome Originale se presente]"
alias: ["Nome in Italiano"]
tier: [0/1/2/3]
---

# [Nome Arma in Italiano]

*[Descrizione narrativa invariata]*

---
### STATISTICHE DAGGERHEART
- **Tier:** [Tier X]
- **Tratto per l'Attacco:** [Tratto]
- **Gittata:** [Gittata]
- **Danno:** [Dado e Tipo Danno]
- **Mani:** [Una Mano / Due Mani]

### CARATTERISTICHE E TRATTI SPECIALI
- **[Nome Tratto]:** [Descrizione dell'effetto meccanico in stile Daggerheart].

Non inserire blocchi ```markdown, restituisci solo il testo pulito.
"""

def query_ollama(prompt, content):
    url = "http://172.16.1.163:11434/api/generate"
    payload = {
        "model": "qwen3.6:35b",
        "system": prompt,
        "prompt": content,
        "stream": False,
        "options": {
            "temperature": 0.2
        }
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode('utf-8'))
        return result.get("response", "")

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith('.md')]
    if not files:
        print(f"⚠️ Nessun file .md trovato in {SOURCE_DIR}")
        return

    print(f"🦙 Avvio conversione LOCALE (Ollama / qwen2.5) di {len(files)} armi...\n")

    for index, filename in enumerate(files, 1):
        src_file = os.path.join(SOURCE_DIR, filename)
        dest_file = os.path.join(OUTPUT_DIR, filename)

        if os.path.exists(dest_file):
            print(f"[{index}/{len(files)}] ⏩ Già convertito: {filename}")
            continue

        with open(src_file, 'r', encoding='utf-8') as f:
            content = f.read()

        print(f"[{index}/{len(files)}] 🔄 Convertendo in locale: {filename}...")

        try:
            response_text = query_ollama(SYSTEM_PROMPT, content)

            clean_text = re.sub(r'^```markdown\n', '', response_text)
            clean_text = re.sub(r'^```\n', '', clean_text)
            clean_text = re.sub(r'\n```$', '', clean_text)

            with open(dest_file, 'w', encoding='utf-8') as f:
                f.write(clean_text)

            print("   ✅ Completato!")

        except Exception as e:
            print(f"   ❌ Errore (assicurati che Ollama sia attivo): {e}")

    print("\n🎉 Operazione completata! Controlla la cartella Armi_Daggerheart.")

if __name__ == "__main__":
    main()
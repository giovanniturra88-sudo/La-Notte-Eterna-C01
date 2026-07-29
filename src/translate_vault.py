import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from openai import OpenAI

# ---------------------------------------------------------------------------
# CONFIGURAZIONE AMBIENTE LOCALE / RETE (DGX SPARKS)
# ---------------------------------------------------------------------------
# Client OpenAI collegato alla tua istanza locale sul DGX
# Nota: Modifica la porta in base al tuo server (es. :11434 per Ollama, :8000 per vLLM)
client = OpenAI(
    base_url="http://172.16.1.163:11434/v1",
    api_key="ollama"  # Key fittizia per server locale
)

MODEL_NAME = "qwen3.6:35b"

# Cartelle del Vault Obsidian (Punti di origine e destinazione per le Armature)
SOURCE_DIR = "./02_Meccaniche_DaggerHeart/Armi"
OUTPUT_DIR = "./02_Meccaniche_DaggerHeart/Armi_IT"

# Numero di file elaborati contemporaneamente in parallelo
MAX_WORKERS = 4

# ---------------------------------------------------------------------------
# SYSTEM PROMPT PER QWEN (ADATTAMENTO ARMATURE DAGGERHEART)
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = """
Sei un traduttore esperto di Giochi di Ruolo (TTRPG) ed esperto dell'editor Obsidian.
Il tuo compito è tradurre il file Markdown fornito dall'inglese all'italiano, ADATTANDO contestualmente le meccaniche al regolamento di Daggerheart.

REGOLE TASSATIVE DI TRADUZIONE ED ADATTAMENTO:
1. FRONTMATTER YAML (Intestazione):
   - Mantieni la struttura compresa tra i delimitatori --- e ---.
   - Aggiungi la proprietà 'original_name:' che deve contenere il nome originale in inglese del file/oggetto (es. original_name: "Advanced Full Plate Armor").
   - Aggiungi la proprietà 'alias:' contenente una lista con il nome tradotto in italiano (es. alias: ["Armatura Completa Avanzata"]).

2. CONTENUTO E MECCANICHE GAMEPLAY:
   - Traduci il testo narrativo in un italiano fluido, naturale ed epico.
   - Adatta la terminologia al sistema Daggerheart:
     * "Armor Score / AC" -> "Punteggio Armatura"
     * "Damage Thresholds" -> "Soglie di Danno" (Minor / Major / Severe)
     * "Evasion Penalty" -> "Penalità all'Evasione"
     * "Slot / Burden" -> "Ingombro / Slot"
     * "Feature / Effect / Ability" -> "Tratto dell'Armatura / Effetto"

3. SINTASSI OBSIDIAN:
   - Preserva la sintassi dei link bidirezionali [[...]].
   - Mantieni intatta la struttura delle intestazioni (#, ##, ###) e delle liste puntate.

4. OUTPUT:
   - Restituisci ESCLUSIVAMENTE il contenuto del file Markdown finale tradotto.
   - NON aggiungere commenti, scuse, spiegazioni o blocchi di codice prima o dopo il testo.
"""

# ---------------------------------------------------------------------------
# FUNZIONI DI ELABORAZIONE
# ---------------------------------------------------------------------------
def translate_file(filename):
    src_file = os.path.join(SOURCE_DIR, filename)
    dest_file = os.path.join(OUTPUT_DIR, filename)

    with open(src_file, 'r', encoding='utf-8') as f:
        content = f.read()

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": content}
            ],
            temperature=0.2, # Bassa temperatura per massima stabilità su tag e formattazione
        )
        
        translated_content = response.choices[0].message.content

        # Pulizia di eventuali delimitatori ```markdown o ``` restituiti dal modello
        clean_text = re.sub(r'^```markdown\n', '', translated_content)
        clean_text = re.sub(r'^```\n', '', clean_text)
        clean_text = re.sub(r'\n```$', '', clean_text)

        with open(dest_file, 'w', encoding='utf-8') as f:
            f.write(clean_text)

        return f"✅ Salvato: {filename}"

    except Exception as e:
        return f"❌ Errore durante l'elaborazione di {filename}: {e}"

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith('.md')]
    
    if not files:
        print(f"⚠️ Nessun file .md trovato nella cartella sorgente: {SOURCE_DIR}")
        return

    print(f"🚀 Avvio traduzione di {len(files)} file con {MODEL_NAME} su DGX (Parallelismo: {MAX_WORKERS})...\n")

    # Esecuzione multithreading in parallelo
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(translate_file, filename): filename for filename in files}
        for future in as_completed(futures):
            print(future.result())

    print("\n🎉 Elaborazione completata! I file tradotti si trovano in:", OUTPUT_DIR)

if __name__ == "__main__":
    main()
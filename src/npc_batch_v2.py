import requests
import json
import csv
import re
from pathlib import Path

# ==========================
# CONFIGURAZIONE
# ==========================

OLLAMA_URL = "http://172.16.1.163:11434/api/generate"
MODEL = "qwen3.6:35b"


NPC_DIR = Path(r"03_Campagna\PNG")

# ==========================
# NORMALIZZAZIONE STATUS
# ==========================

def normalize_status(value):

    if value is None:
        return "unknown"

    value = str(value).strip().lower()

    if value in [
        "alive",
        "vivo",
        "living"
    ]:
        return "alive"

    if value in [
        "dead",
        "morto"
    ]:
        return "dead"

    if any(x in value for x in [
        "undead",
        "morto vivente",
        "vampir"
    ]):
        return "undead"

    return "unknown"


# ==========================
# ESTRAZIONE JSON
# ==========================

def extract_json(text):

    text = text.strip()

    try:
        return json.loads(text)
    except:
        pass

    match = re.search(
        r"\{.*\}",
        text,
        re.DOTALL
    )

    if match:
        return json.loads(match.group(0))

    raise ValueError("JSON non trovato")


# ==========================
# PROCESSING
# ==========================

rows = []

for md in sorted(NPC_DIR.glob("*.md")):

    print(f"\nAnalizzo {md.name}")

    text = md.read_text(
        encoding="utf-8"
    )

    prompt = f"""
    Analizza questa scheda NPC della campagna Notte Eterna.

    Estrai esclusivamente:

    - aliases
    - faction
    - location
    - status

    REGOLE OBBLIGATORIE

    1. Rispondi SOLO con JSON valido.

    2. NON aggiungere spiegazioni.

    3. NON aggiungere commenti.

    4. NON usare markdown.

    5. NON restituire testo prima o dopo il JSON.

    6. Se una informazione non è presente usa null.

    7. aliases deve contenere SOLO:
    - soprannomi
    - titoli ufficiali
    - nomi alternativi esplicitamente presenti

    ESEMPI CORRETTI:
    - Matrona di Sangue
    - Signore dei Falchi

    ESEMPI ERRATI:
    - famelico come un lupo
    - santo
    - messia
    - organizzazione
    - predatrice

    8. faction deve essere il NOME ESATTO di una fazione.

    ESEMPI CORRETTI:
    - Armata dell'Apocalisse
    - Chiesa di Garod
    - Custodi dei Segreti
    - Ordine dei Predestinati

    ESEMPI ERRATI:
    - religione
    - organizzazione
    - fazione
    - esercito
    - regno
    - impero
    - ordine
    - tribù

    Se trovi soltanto la categoria ma NON il nome della fazione, usa null.

    9. location deve essere il luogo principale associato al personaggio.

    ESEMPI:
    - Neir
    - Città delle Trame
    - Verde Foresta
    - Forte Arundex

    10. status può essere SOLO uno dei seguenti valori:

    alive
    dead
    undead
    unknown

    11. Vampiri, lich, non morti e creature non morte hanno status = undead.

    12. Se il personaggio è vivo usa alive.

    13. Se il personaggio è morto usa dead.

    14. Se non è possibile determinarlo usa unknown.

    OUTPUT OBBLIGATORIO

    {{
    "aliases": [],
    "faction": null,
    "location": null,
    "status": "unknown"
    }}

    TESTO NPC

    {text}
    """

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "think": False,
                "options": {
                    "temperature": 0.1,
                    "top_p": 0.2,
                    "num_predict": 120
                }
            },
            timeout=600
        )

        raw = response.json()["response"]

        data = extract_json(raw)

        aliases = data.get(
            "aliases",
            []
        )

        if aliases is None:
            aliases = []

        faction = data.get("faction")
        location = data.get("location")
        status = normalize_status(
            data.get("status")
        )

        rows.append(
            {
                "name": md.stem,
                "aliases": ";".join(
                    aliases
                ),
                "faction": faction,
                "location": location,
                "status": status
            }
        )

        print("OK")

    except Exception as e:

        print(
            f"ERRORE {md.name}: {e}"
        )

        rows.append(
            {
                "name": md.stem,
                "aliases": "",
                "faction": "",
                "location": "",
                "status": "unknown"
            }
        )

# ==========================
# CSV
# ==========================

with open(
    "npc_metadata.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.DictWriter(
        f,
        fieldnames=[
            "name",
            "aliases",
            "faction",
            "location",
            "status"
        ]
    )

    writer.writeheader()
    writer.writerows(rows)

print("\nCreato npc_metadata.csv")
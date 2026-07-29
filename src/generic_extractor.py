import requests
import json
import csv
import re
from pathlib import Path

# =====================================================
# CONFIGURAZIONE
# =====================================================

OLLAMA_URL = "http://172.16.1.163:11434/api/generate"
MODEL = "qwen3.6:35b"

MODE = "location"

# npc
# location
# artifact
# deity

# =====================================================
# MODALITA'
# =====================================================

CONFIG = {

    "npc": {

        "source_dir": Path(r"03_Campagna\PNG"),

        "output_csv": "npc_metadata.csv",

        "prompt": """
Analizza questa scheda NPC.

Rispondi SOLO con JSON.

{
  "aliases": [],
  "faction": null,
  "location": null,
  "status": "unknown"
}

status:
alive
dead
undead
unknown

TESTO:

{text}
"""
    },

    "location": {

        "source_dir": Path(r"01_Lore\Geografia"),

        "output_csv": "location_metadata.csv",

"prompt": """
Analizza questa location della campagna Notte Eterna.

Rispondi ESCLUSIVAMENTE con JSON valido.

Estrai:

- region
- parent_location
- controlling_faction
- controlling_people
- location_type

REGOLE

region:
macroregione principale.

Esempi:
- Neir
- Cenere di Lanie
- Valle Nuvolosa
- Larass'hra

parent_location:
contenitore geografico diretto.

Esempi:
- Öuin
- Città delle Trame
- Gloriosa Ezakran

controlling_faction:
organizzazione, chiesa, ordine, gilda,
esercito o istituzione.

Esempi corretti:
- Chiesa di Garod
- Custodi dei Segreti
- Ordine dei Predestinati
- Prescelti delle Tenebre
- Ospedalieri

Esempi errati:
- karevi
- hjilaki
- urakian
- nani
- draghi rossi

controlling_npc:
personaggio specifico che governa,
possiede o domina il luogo.

Esempi:

- Namass'rya
- Efneriom
- Annie Rose-Robe

NON usare questo campo per:
- fazioni
- popoli
- religioni

controlling_people:
popolo, specie, etnia o cultura.

Esempi:
- karevi
- hjilaki
- urakian
- klorss
- nani
- draghi rossi

location_type può essere:

continent
region
kingdom
empire
nation
province
city
village
fortress
forest
mountain
island
landmark
building
temple
institution
unknown

Se un dato non è presente usa null.

Output obbligatorio:

{
  "region": null,
  "parent_location": null,
  "controlling_faction": null,
  "controlling_people": null,
  "controlling_npc": null,
  "location_type": "unknown"
}

TESTO:

{text}
"""
    },

    "artifact": {

        "source_dir": Path(
            r"01_Lore\Cosmologia\Meteore"
        ),

        "output_csv": "artifact_metadata.csv",

        "prompt": """
Analizza questo artefatto.

Rispondi SOLO con JSON.

{
  "artifact_type": null,
  "current_owner": null,
  "current_location": null
}

TESTO:

{text}
"""
    },

    "deity": {

        "source_dir": Path(
            r"01_Lore\Divinità_e_Fazioni"
        ),

        "output_csv": "deity_metadata.csv",

        "prompt": """
Analizza questa voce.

Rispondi SOLO con JSON.

{
  "category": null,
  "alignment": null,
  "related_locations": []
}

category:
deity
faction

alignment:
light
neutral
dark
unknown

TESTO:

{text}
"""
    }
}

cfg = CONFIG[MODE]

# =====================================================
# JSON CLEANER
# =====================================================

def extract_json(text):

    text = text.strip()

    try:
        return json.loads(text)
    except:
        pass

    m = re.search(
        r"\{.*\}",
        text,
        re.DOTALL
    )

    if m:
        return json.loads(m.group())

    raise ValueError("JSON not found")

# =====================================================
# PROCESSING
# =====================================================

rows = []

files = list(
    cfg["source_dir"].rglob("*.md")
)

print(
    f"Trovati {len(files)} file"
)

for md in files:

    print(
        f"Analizzo: {md.name}"
    )

    text = md.read_text(
        encoding="utf-8"
    )

    prompt = cfg["prompt"].replace(
        "{text}",
        text
    )

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
                    "num_predict": 200
                }
            },
            timeout=600
        )

        raw = response.json()["response"]

        data = extract_json(raw)

        data["name"] = md.stem

        rows.append(data)

    except Exception as e:

        print(
            md.name,
            e
        )

# =====================================================
# CSV
# =====================================================

fieldnames = set()

for row in rows:
    fieldnames.update(
        row.keys()
    )

fieldnames = sorted(
    fieldnames
)

with open(
    cfg["output_csv"],
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.DictWriter(
        f,
        fieldnames=fieldnames
    )

    writer.writeheader()

    for row in rows:
        writer.writerow(row)

print(
    f"\nCreato {cfg['output_csv']}"
)
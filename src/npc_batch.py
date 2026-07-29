import requests
import json
import csv
from pathlib import Path

OLLAMA_URL = "http://172.16.1.163:11434/api/generate"
MODEL = "qwen3.6:35b"

NPC_DIR = Path(r"03_Campagna\PNG")

rows = []

for md in NPC_DIR.glob("*.md"):

    print("Analizzo:", md.name)

    text = md.read_text(
        encoding="utf-8"
    )

    prompt = f"""
Analizza la seguente scheda NPC.

Restituisci SOLO JSON valido.

Campi:

aliases
faction
location
status

Non spiegare.
Non ragionare.
Non aggiungere testo.
Non usare markdown.

Se un valore non è presente usa null.
{text}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "think": False
        },
        timeout=600
    )

    try:

        result = response.json()["response"]

        data = json.loads(result)

        rows.append({
            "name": md.stem,
            "aliases": ";".join(
                data.get("aliases", [])
            ),
            "faction": data.get("faction"),
            "location": data.get("location"),
            "status": data.get("status")
        })

    except Exception as e:

        print(
            "ERRORE:",
            md.name,
            e
        )

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

print("Creato npc_metadata.csv")
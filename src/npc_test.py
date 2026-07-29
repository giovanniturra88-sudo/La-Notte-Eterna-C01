import requests
from pathlib import Path

text = Path(
    r"03_Campagna\PNG\Namass'rya.md"
).read_text(
    encoding="utf-8"
)

prompt = f"""
Analizza questo NPC.

Estrai SOLO:

- aliases
- faction
- location
- status

Rispondi esclusivamente con JSON valido.

Testo:

{text}
"""

response = requests.post(
    "http://172.16.1.163:11434/api/generate",
    json={
        "model": "qwen3.6:35b",
        "prompt": prompt,
        "stream": False
    },
    timeout=600
)

print(response.json()["response"])
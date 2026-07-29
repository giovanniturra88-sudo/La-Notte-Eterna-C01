from pathlib import Path
import re
import requests

# CONFIGURAZIONE

VAULT = Path(r"C:\Users\gturra\DaggerHeart\La Notte Eterna C01\02_Meccaniche_DaggerHeart\adversaries")
OUTPUT = Path(r"c:\Users\gturra\DaggerHeart\La Notte Eterna C01 IT\adversaries")

MODEL = "qwen3-coder-copilot:latest"
OLLAMA_URL = "http://172.16.1.163:11434/api/generate"


def protect_links(text):
    links = {}

    def replace(match):
        token = f"LINK_{len(links)}"
        links[token] = match.group(0)
        return token

    text = re.sub(r"\[\[[^\]]+\]\]", replace, text)

    return text, links


def restore_links(text, links):
    for token, original in links.items():
        text = text.replace(token, original)

    return text


def translate(text):

    prompt = f"""
            Traduci il seguente testo markdown dall'inglese all'italiano, se il suo contenuto è principalmente in inglese.

            Regole:
            - Non modificare i wikilink e i link
            - Mantieni il markdown
            - Non aggiungere commenti
            - Non aggiungere spiegazioni
            - Restituisci solo il testo tradotto

            TESTO:

            {text}
            """

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=1800
    )

    response.raise_for_status()

    return response.json()["response"]


def process_file(md_file):

    relative = md_file.relative_to(VAULT)

    output_file = OUTPUT / relative

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    original = md_file.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    protected, links = protect_links(original)

    translated = translate(protected)

    translated = restore_links(
        translated,
        links
    )

    output_file.write_text(
        translated,
        encoding="utf-8"
    )

    print(f"OK  {relative}")


def main():

    files = list(VAULT.rglob("*.md"))

    print(f"Trovati {len(files)} file")

    for md_file in files:
        try:
            process_file(md_file)
        except Exception as e:
            print(f"ERRORE {md_file}: {e}")


if __name__ == "__main__":
    main()
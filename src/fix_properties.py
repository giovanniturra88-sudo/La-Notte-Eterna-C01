import re
from pathlib import Path

ROOT = Path("02_Meccaniche_Daggerheart/Abilità/")

def extract_metadata(header):

    livello_match = re.search(
        r"Livello\s+(\d+)",
        header,
        re.IGNORECASE
    )

    costo_match = re.search(
        r"Costo di Richiamo.*?(\d+)",
        header,
        re.IGNORECASE
    )

    dominio_match = re.search(
        r"\[\[([^\]]+)\]\]",
        header
    )

    if not (
        livello_match
        and costo_match
        and dominio_match
    ):
        return None

    livello = livello_match.group(1)
    costo = costo_match.group(1)
    dominio = dominio_match.group(1)

    tipologia = None

    #
    # CASO:
    # Abilità [[Grazia]]
    # Magia di [[Grazia]]
    #

    before_domain = header[:dominio_match.start()]

    before_domain = re.sub(
        r"[*_`]",
        " ",
        before_domain
    )

    words = re.findall(
        r"[A-Za-zÀ-ÖØ-öø-ÿ]+",
        before_domain
    )

    ignore = {
        "Livello",
        "Costo",
        "Richiamo",
        "di",
        "d"
    }

    for word in reversed(words):
        if word not in ignore:
            tipologia = word
            break

    #
    # CASO:
    # [[Codice]] Spell
    #

    if tipologia in (
        dominio,
        "Livello"
    ) or not tipologia:

        after_domain = header[
            dominio_match.end():
        ]

        match = re.search(
            r"([A-Za-zÀ-ÖØ-öø-ÿ]+)",
            after_domain
        )

        if match:
            tipologia = match.group(1)

    if not tipologia:
        return None

    return {
        "Livello": livello,
        "Dominio": dominio,
        "Costo di Richiamo": costo,
        "Tipologia Carta": tipologia
    }


def remove_frontmatter(content):

    return re.sub(
        r"^---\s*\n.*?\n---\s*\n?",
        "",
        content,
        flags=re.DOTALL
    )


def build_frontmatter(data):

    return f"""---
Livello: {data['Livello']}
Dominio: "[[{data['Dominio']}]]"
Costo di Richiamo: {data['Costo di Richiamo']}
Tipologia Carta: "[[{data['Tipologia Carta']}]]"
Titolo Inglese:
---

"""


def process_file(file_path):

    content = file_path.read_text(
        encoding="utf-8"
    )

    content = remove_frontmatter(
        content
    )

    lines = content.splitlines()

    first_line = None
    first_index = None

    for idx, line in enumerate(lines):
        if line.strip():
            first_line = line.strip()
            first_index = idx
            break

    if first_line is None:
        return

    metadata = extract_metadata(
        first_line
    )

    if metadata is None:
        print(
            f"[ERRORE] {file_path.name}"
        )
        print(first_line)
        return

    body = "\n".join(
        lines[first_index + 1:]
    ).strip()

    new_content = (
        build_frontmatter(metadata)
        + body
        + "\n"
    )

    file_path.write_text(
        new_content,
        encoding="utf-8"
    )

    print(
        f"OK {file_path.name}"
    )


def main():

    files = sorted(
        ROOT.glob("*.md")
    )

    for file_path in files:
        process_file(file_path)

    print("Fine elaborazione")


if __name__ == "__main__":
    main()
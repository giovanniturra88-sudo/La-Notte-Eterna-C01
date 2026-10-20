# SPEC — Struttura cartella avventura (basata su A01_La_Morte_Strisciante)

Ogni avventura in `04_Risorse/Campagna/storylines/*.pdf` va trasposta in una cartella
`05_StoryLines/A0X_<Nome>.md` (cartella) con la stessa logica e struttura di
`05_StoryLines/A01_La_Morte_Strisciante`. Tutto in **italiano**.

## Struttura cartella
```
05_StoryLines/
  <Nome>.md                      # file indice (tipo Indice)
  A0X_<Nome>/                    # cartella avventura
    A0X_<Nome>.md               # indice cartella (tipo Indice, dataview LIST)
    Overview.md                 # tipo Storyline
    Conversione Daggerheart.md  # conversione meccaniche 5e -> Daggerheart
    Agganci/                    # (può restare vuota)
    Creature/                   # una .md per mostro/creatura
    Gruppi e Fazioni Operative/ # una .md per gruppo/fazione
    Luoghi/                     # una .md per luogo
    PNG/                        # una .md per PNG
    Scene/                      # S01..SNN - <Nome Scena>.md
    Sorgenti/                   # (può restare vuota)
```

## 1. File indice `05_StoryLines/<Nome>.md`
```
---
type:
 - "Indice"
---

# <Nome>

<frase descrittiva breve dell'avventura>

## Capitolo
- [[A0X_<Nome>]]

## Citata da
```dataview
LIST
FROM "."
WHERE contains(file.inlinks, this.file.link)
```
```

## 2. `A0X_<Nome>/A0X_<Nome>.md` (indice cartella)
```
---
type:
 - "Indice"
---

# A0X <Nome>

## Contenuto della cartella
```dataview
LIST
FROM "05_StoryLines/A0X_<Nome>"
WHERE file.name != this.file.name
SORT file.name ASC
```
```

## 3. `A0X_<Nome>/Overview.md` (tipo Storyline)
Frontmatter:
```
---
type: Storyline
aliases:
 - "<Nome>"
status: Canonica
livello_consigliato: <livelli>
ambientazione:
 - "[[<Luogo>]]"
---
```
Sezioni:
- `# <Nome>`
- `## Riassunto` (2-4 frasi)
- `## PNG Principali` (lista [[...]])
- `## Luoghi Principali` (lista [[...]])
- `## Storyline` (lista [[S01 - ...]] ... [[SNN - ...]])
- `## Epilogo` (paragrafo)

## 4. `A0X_<Nome>/Conversione Daggerheart.md`
Conversione delle meccaniche 5e in Daggerheart. Sezioni tipiche:
- `## Panoramica`
- `# Fronti Narrativi` (per ogni fronte: `### Domanda`, `### Minaccia`, `### Escalation` (lista numerata), `### Risoluzione`)
- `# Clock Narrativi` (per ogni clock: `○ ○ ○ ○ ○ ○`, "Si riempie quando:", "Effetto finale:")
- `# Fazioni Coinvolte`
- `# Luoghi Chiave`
- `# Tematiche`
- `# Avversari Daggerheart` (per ogni nemico: `### Ruolo`, `### Tipo`, `### Comportamento`, `### Fear Move`, `### Obiettivo`, `### Sconfitta`)
Nota: le avventure sono 5e OGL; la conversione è una reinterpretazione in termini
Daggerheart (Hope/Fear, Clock, Fear Move). Se non è possibile convertire con certezza,
scrivere una conversione plausibile e coerente con il tono dell'avventura.

## 5. `A0X_<Nome>/Scene/SNN - <Nome Scena>.md`
Frontmatter:
```
---
type: StorylineScene
storyline:
 - "[[<Nome>]]"
---
```
Sezioni (usare quelle pertinenti):
- `# <Nome Scena>`
- `## Situazione` / `## Scopo`
- `## Obiettivo`
- `## Luogo`
- `## PNG Coinvolti`
- `## Cosa apprendono i PG`
- `## Indizi`
- `## Segreti`
- `## Atmosfera`
- `## Ricompensa`
- `## Prossime Scene` (lista [[SNN - ...]])
Trascrivere il contenuto della scena dal PDF in modo completo.

## 6. `A0X_<Nome>/PNG/<Nome PNG>.md`
Frontmatter:
```
---
type:
 - "[[PNG]]"
storyline:
 - "[[<Nome>]]"
luoghi:
 - "[[<Luogo>]]"
---
```
Sezioni:
- `# <Nome PNG>`
- `## Ruolo`
- `## Descrizione`
- `## Personalità` (lista)
- `## Storia`
- `## Obiettivi` (### Pubblici / ### Reali o ### Segreti)
- `## Segreti`
- `## Relazioni` (### Alleati / ### Nemici / ...)
- `## Punto Debole`
- `## Coinvolgimento nella Storyline` (per scena)
- `## Citazione` (blockquote)

## 7. `A0X_<Nome>/Creature/<Nome>.md`
Frontmatter:
```
---
type:
 - "[[Creatura]]"
storyline:
 - "[[<Nome>]]"
---
```
Sezioni:
- `# <Nome>`
- `## Descrizione`
- `## Aspetto`
- `## Comportamento`
- `## Origine`
- `## Nella Notte Eterna`
- `## Storyline Coinvolte`
- `## Collegamenti`
- `## Statistiche Daggerheart` (se convertibile: Rango, Difficoltà, Soglie, Punti Ferita, Stress, Esperienza, Attacchi, Tratti, Capacità)

## 8. `A0X_<Nome>/Luoghi/<Nome>.md`
Frontmatter:
```
---
type: Luogo
---
```
Sezioni:
- `# <Nome>`
- `## Descrizione`
- `## Atmosfera`
- `## Pericoli`
- `## Collegamenti`
(oppure segnaposto se non sviluppato)

## 9. `A0X_<Nome>/Gruppi e Fazioni Operative/<Nome>.md`
Frontmatter:
```
---
type:
 - "[[Creatura]]"
 - "[[Organizzazioni]]"
storyline:
 - "[[<Nome>]]"
---
```
Sezioni:
- `# <Nome>`
- `## Ruolo`
- `## Descrizione`
- `## Personalità`
- `## Storia`
- `## Obiettivi`
- `## Segreti`
- `## Relazioni`
- `## Coinvolgimento nella Storyline`
- `## Citazione`

## Regole generali
- Tutto in italiano.
- Usare [[...]] per i link wiki tra entità (PNG, luoghi, creature, fazioni, storyline).
- Non inventare contenuti non presenti nel PDF; se un dato manca, omettere la sezione.
- La trascrizione deve essere completa e fedele al PDF.
- I file PNG/Creature/Scene/Luoghi/Gruppi vanno creati in base a ciò che il PDF contiene.
- Non creare file con contenuto vuoto: se una sezione non ha contenuto, omettila.

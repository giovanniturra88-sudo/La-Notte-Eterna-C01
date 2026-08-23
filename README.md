# 🌑 La Notte Eterna — Vault DaggerHeart

Vault Obsidian per la campagna **"La Notte Eterna"**, giocata con il sistema **DaggerHeart**.

## 🎯 Scopo

Questo vault raccoglie tutto il materiale necessario per gestire la campagna:

- **Lore e ambientazione** del mondo di gioco
- **Meccaniche e regole** del sistema DaggerHeart
- **Materiale homebrew** adattato da DnD a DaggerHeart
- **Strumenti di gestione** per il Master (dashboard, sessioni, storyline)

## 📁 Struttura delle Cartelle

| Cartella | Contenuto |
|---|---|
| `00_Dashboard/` | Dashboard, indici e strumenti di gestione della campagna |
| `01_Lore/` | Ambientazione, cosmologia, divinità, geografia, razze, cronologia |
| `02_Meccaniche_Daggerheart/` | **Materiale ufficiale del sistema DaggerHeart** (regole, classi, armi, nemici) |
| `03_Campagna/` | Documento principale della campagna, luoghi di gioco, sessioni |
| `04_Risorse/` | Immagini e template riutilizzabili |
| `05_StoryLines/` | Archi narrativi e storyline |
| `06_Materiale_Notte_Eterna/` | **Materiale homebrew della campagna**, adattato da DnD a DaggerHeart |

## 🔑 Distinzione Fondamentale: `02` vs `06`

- **`02_Meccaniche_Daggerheart/`** → Materiale **ufficiale** del gioco DaggerHeart. È il riferimento di sistema: non va modificato.
- **`06_Materiale_Notte_Eterna/`** → Materiale **della campagna**, creato dal Master e adattato da DnD a DaggerHeart. È il contenuto homebrew che va consultato per le partite.

> ⚠️ **Regola**: se un contenuto è ufficiale DaggerHeart, va in `02`. Se è un adattamento o una creazione per la campagna, va in `06`.

## 🗂️ Convenzioni di Denominazione

- **Lingua**: tutti i nomi di file e note in **italiano**
- **Formato**: `Nome della Nota.md` (spazi e capitalizzazione standard)
- **Evitare**: acronimi, codici, doppie lingue (es. `Shadow Hunter.md` → `Cacciatore delle Ombre.md`)

## 🧩 Template Disponibili

I template si trovano in `04_Risorse/Templates/`:

| Template | Uso |
|---|---|
| `Template Ancestry.md` | Creazione di una nuova Ancestry |
| `Template Avversario.md` | Creazione di un nemico/avversario |
| `Template Scena.md` | Creazione di una scena di gioco |

## 🔗 Link e Frontmatter

- Tutti i collegamenti tra note usano la sintassi Obsidian `Nome Nota`
- Ogni nota dovrebbe avere un frontmatter YAML con `type` e, se necessario, `aliases`

## 🚀 Per Iniziare

1. Apri `00_Dashboard/Home.md` per il dashboard principale
2. Consulta `03_Campagna/La Notte Eterna.md` per il documento di campagna
3. Usa i template in `04_Risorse/Templates/` per creare nuovo materiale
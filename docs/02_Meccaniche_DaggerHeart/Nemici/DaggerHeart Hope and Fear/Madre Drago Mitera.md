---
type:
  - "[[Creatura]]"
  - "[[Solo]]"
aliases:
 - "Dragon Mother Mitera"
---

## Madre Drago Mitera
* **Descrizione:** Un drago gargantuesco a sette teste, con squame di diamante scintillanti che brillano con ogni colore dell'arcobaleno.
* **Rango:** 4 (Solo)
* **Difficoltà:** 16
* **Soglie di Danno:** 35/65
* **Punti Ferita:** 12 | **Stress:** 10
* **Esperienza:** Antico +5
* **Attacchi:**
 * **Morso e Taglio:** +8 | Ravvicinata | 4d10+10 fisico
* **Tratti e Capacità:**
 * **Inesorabile (3) - Passiva:** Mitera può essere messa a fuoco fino a tre volte per turno del GM. Spendere Paura come di consueto per metterla a fuoco.
 * **Pelle di Diamante - Passiva:** Conto alla rovescia (7). Quando Mitera appare per la prima volta, attiva il conto alla rovescia. Mitera guadagna un bonus alla sua Difficoltà pari al valore attuale del dado del conto alla rovescia. Si riduce tramite la capacità "Sette Teste" di Mitera. Quando il conto alla rovescia scatta, Mitera diventa *Vulnerabile* e guadagna un bonus di +2 ai tiri d'attacco.
 * **Soffio Elementale - Azione:** Segnare uno Stress per far scatenare a Mitera energia elementale da una testa a tua scelta:
 1. **Fuoco.** Infliggi 4d12 danni magici a 1d4+1 bersagli entro portata Ravvicinata. I bersagli che subiscono danni devono segnare una Casella Armatura o 2 PF aggiuntivi.
 2. **Fulmine.** Infliggi 4d12 danni magici a 1d6 bersagli entro portata Lontana, purché ogni bersaglio oltre il primo sia entro portata Ravvicinata del bersaglio precedente.
 3. **Acido.** Ogni PG davanti a Mitera entro portata Ravvicinata deve effettuare un Tiro di Reazione di Agilità. I bersagli che falliscono devono segnare 2 Caselle Armatura e 2 PF. I bersagli che riescono devono segnare una Casella Armatura e un PF.
 4. **Veleno.** Una miasma di gas tossico di palude *Maledice* tutti i bersagli entro portata Ravvicinata di Mitera. Mentre è *Maledetto*, un bersaglio ha svantaggio sui tiri di azione finché non segna 1d4 Stress per rimuovere la condizione.
 5. **Ghiaccio.** Ogni bersaglio davanti a Mitera entro portata Ravvicinata subisce 4d8+8 danni magici ed è *Trattenuto* dal ghiaccio finché non si libera con un Tiro di Forza riuscito. Inoltre, quest'area si congela e un PG deve superare un Tiro di Reazione di Agilità per attraversarla.
 6. **Oscurità.** Una nuvola di ombra magica riempie un'area entro portata Ravvicinata. Le creature all'interno della nuvola, tranne Mitera, sono *Vulnerabili* e hanno svantaggio sui tiri di azione che si basano sulla vista. La nuvola si dissipa quando questa opzione di Soffio Elementale viene rimossa dalla capacità "Sette Teste" di Mitera.
 7. **Luce.** Un raggio di pura energia luminosa infligge 28 danni magici diretti a ogni creatura in una linea entro portata Remota.
 * **Sferzata della Coda - Azione:** Spendere una Paura per attaccare tutti i bersagli entro portata Ravvicinata. I bersagli contro cui l'attacco ha successo subiscono 2d20+10 danni fisici e vengono respinti in portata Lontana. I bersagli che segnano PF da questo attacco diventano *Vulnerabili* finché non rimuovono un PF. I bersagli contro cui l'attacco è fallito devono segnare uno Stress.
 * **Spaventosa - Reazione:** Quando Mitera effettua un tiro d'attacco riuscito contro un PG o un PG fallisce un tiro entro portata Lontana, guadagni una Paura.
 * **Sette Teste - Reazione:** Quando Mitera subisce danni, tira un d8. Rimuovi permanentemente l'opzione di "Soffio Elementale" che corrisponde al risultato. Con un risultato di 8, o se l'opzione corrispondente è già stata rimossa, riduci il conto alla rovescia di Pelle di Diamante (vedi "Pelle di Diamante").

```statblock
layout: DaggerHeart Nemici
name: "Madre Drago Mitera"
description: "Un drago gargantuesco a sette teste, con squame di diamante scintillanti che brillano con ogni colore dell'arcobaleno."
tier: "4"
ruolo: "Solo"
difficolta: "16"
hp: "12"
stress: "10"
esperienza: "Antico +5"
soglia_danni: "35/65"
attacchi:
  - name: "Morso e Taglio"
    desc: "**+8** | Ravvicinata | **4d10+10** fisico"
tratti:
  - name: "Inesorabile (3)"
    desc: "*- Passiva:* Mitera può essere messa a fuoco fino a tre volte per turno del GM. Spendere Paura come di consueto per metterla a fuoco."
  - name: "Pelle di Diamante"
    desc: "*- Passiva:* Conto alla rovescia (7). Quando Mitera appare per la prima volta, attiva il conto alla rovescia. Mitera guadagna un bonus alla sua Difficoltà pari al valore attuale del dado del conto alla rovescia. Si riduce tramite la capacità 'Sette Teste' di Mitera. Quando il conto alla rovescia scatta, Mitera diventa *Vulnerabile* e guadagna un bonus di +2 ai tiri d'attacco."
capacita_speciali:
  - name: "Soffio Elementale"
    desc: "*- Azione:* Segnare uno Stress per far scatenare a Mitera energia elementale da una testa a tua scelta: Fuoco, Fulmine, Acido, Veleno, Ghiaccio, Oscurità, Luce."
  - name: "Sferzata della Coda"
    desc: "*- Azione:* Spendere una Paura per attaccare tutti i bersagli entro portata Ravvicinata. I bersagli contro cui l'attacco ha successo subiscono 2d20+10 danni fisici e vengono respinti in portata Lontana. I bersagli che segnano PF da questo attacco diventano *Vulnerabili* finché non rimuovono un PF. I bersagli contro cui l'attacco è fallito devono segnare uno Stress."
  - name: "Spaventosa"
    desc: "*- Reazione:* Quando Mitera effettua un tiro d'attacco riuscito contro un PG o un PG fallisce un tiro entro portata Lontana, guadagni una Paura."
  - name: "Sette Teste"
    desc: "*- Reazione:* Quando Mitera subisce danni, tira un d8. Rimuovi permanentemente l'opzione di 'Soffio Elementale' che corrisponde al risultato. Con un risultato di 8, o se l'opzione corrispondente è già stata rimossa, riduci il conto alla rovescia di Pelle di Diamante."
```
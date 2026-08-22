---
type:
  - "[[Creatura]]"
  - "[[Orda]]"
---

## Coro Sacro
* **Descrizione:** Un'ostale celeste di umanoidi alati, il cui canto evoca lacrime di devozione religiosa.
* **Tier:** 4 (Orda, 6 PF)
* **Difficoltà:** 17
* **Soglie di Danno:** 24/48
* **Punti Ferita:** 7 | **Stress:** 6
* **Esperienza:** Musica +2
* **Attacchi:**
  * **Detonazione Corale:** +2 | Lontana | 4d10 magico
* **Tratti e Capacità:**
  * **Orda (2d10) - Passiva:** Quando il Coro ha segnato metà o più dei suoi PF, il suo attacco standard infligge 2d10 danni magici.
  * **Coda Celeste - Passiva:** Conto alla Rovina (Loop 3). Il canto divino del Coro si accumula con ogni ritornello. Quando il Coro appare per la prima volta, attiva il conto alla rovina. Si riduce quando un PG guadagna una Speranza. Quando scatta, posiziona un token su questo statblock. Il Coro guadagna un bonus ai tiri sui danni pari al numero di token su questo statblock.
  * **Assalto Aurale - Azione:** Il Coro sfoga la sua energia divina accumulata in un'unica scarica, rimuovendo tutti i token da questo statblock. Infliggi 1d12 danni magici diretti a ogni nemico entro portata Vicina per ogni token rimosso.

```statblock
layout: DaggerHeart Nemici
name: "Coro Sacro"
description: "Un'ostale celeste di umanoidi alati, il cui canto evoca lacrime di devozione religiosa."
tier: "4"
ruolo: "Orda"
difficolta: "17"
hp: "7"
stress: "6"
esperienza: "Musica +2"
soglia_danni: "24/48"
attacchi:
  - name: "Detonazione Corale"
    desc: "**+2** | Lontana | **4d10** magico"
tratti:
  - name: "Orda (2d10)"
    desc: "*- Passiva:* Quando il Coro ha segnato metà o più dei suoi PF, il suo attacco standard infligge 2d10 danni magici."
  - name: "Coda Celeste"
    desc: "*- Passiva:* Conto alla Rovina (Loop 3). Il canto divino del Coro si accumula con ogni ritornello. Quando il Coro appare per la prima volta, attiva il conto alla rovina. Si riduce quando un PG guadagna una Speranza. Quando scatta, posiziona un token su questo statblock. Il Coro guadagna un bonus ai tiri sui danni pari al numero di token su questo statblock."
capacita_speciali:
  - name: "Assalto Aurale"
    desc: "*- Azione:* Il Coro sfoga la sua energia divina accumulata in un'unica scarica, rimuovendo tutti i token da questo statblock. Infliggi 1d12 danni magici diretti a ogni nemico entro portata Vicina per ogni token rimosso."
```
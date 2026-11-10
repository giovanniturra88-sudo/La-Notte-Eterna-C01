---
type:
  - "[[Creatura]]"
  - "[[Ruolo]]"
---

## Nome del Nemico
* **Descrizione:** Breve descrizione narrativa dell'avversario.
* **Rango:** 1 (Ruolo / Descrittore opzionale)
* **Difficoltà:** 12
* **Soglie di Danno:** Minore: 4 | Maggiore: 8 | Grave: 12
* **Punti Ferita:** 4 | **Stress:** 2
* **Esperienza:** Tratto +2
* **Attacchi:**
 * **Nome Attacco 1:** +X | Distanza | XdX+X tipo danno
 * **Nome Attacco 2:** +X | Ravvicinata | XdX+X tipo danno
* **Tratti e Capacità:**
 * **Nome Tratto Passivo:** Descrizione dell'effetto passivo o condizionale.
 * **Nome Mossa (Costo: 1 Paura):** Descrizione dell'abilità speciale che consuma risorse del GM o Stress.

```statblock
layout: DaggerHeart Nemici
name: "Nome del Nemico"
description: "Breve descrizione narrativa dell'avversario."
tier: "1"
ruolo: "Ruolo / Descrittore opzionale"
difficolta: "12"
hp: "4"
stress: "2"
esperienza: "Tratto +2"
soglia_danni: "Minore: 4 | Maggiore: 8 | Grave: 12"
attacchi:
  - name: "Nome Attacco 1"
    desc: "**+X** | Distanza | **XdX+X** tipo danno"
  - name: "Nome Attacco 2"
    desc: "**+X** | Ravvicinata | **XdX+X** tipo danno"
tratti:
  - name: "Nome Tratto Passivo"
    desc: "Descrizione dell'effetto passivo o condizionale."
capacita_speciali:
  - name: "Nome Mossa (Costo: 1 Paura)"
    desc: "Descrizione dell'abilità speciale che consuma risorse del GM o Stress."
```

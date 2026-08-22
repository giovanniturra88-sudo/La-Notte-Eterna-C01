---
type:
  - "[[Creatura]]"
  - "[[Minion]]"
---

## Ombra Tronca
* **Descrizione:** Un'ombra vivente bidimensionale, legata a piani e superfici piane.
* **Tier:** 4 (Minion)
* **Difficoltà:** 19
* **Soglie di Danno:** Nessuna
* **Punti Ferita:** 1 | **Stress:** 2
* **Attacchi:**
  * **Strangolamento:** +3 | Vicina | 10 magico
* **Tratti e Capacità:**
  * **Minion (12) - Passiva:** L'Ombra viene sconfitta quando subisce qualsiasi danno. Per ogni 12 danni che un PG infligge all'Ombra, il PG sconfigge un Minion aggiuntivo entro portata contro cui l'attacco avrebbe successo.
  * **Aggancio dell'Ombra - Azione:** Segnare uno Stress per effettuare un attacco contro un bersaglio entro portata Vicina. In caso di successo, il bersaglio diventa *Vulnerabile* e deve segnare uno Stress quando compie un'azione finché l'Ombra non viene sconfitta.
  * **Attacco di Gruppo - Azione:** Spendere una Paura per scegliere un bersaglio e mettere a fuoco tutte le Ombre Tronche entro portata Vicina di esso. Quei Minion si muovono in portata Da Vicino del bersaglio ed effettuano un tiro d'attacco condiviso. In caso di successo, infliggono 10 danni magici ciascuno. Combina questi danni.

```statblock
layout: DaggerHeart Nemici
name: "Ombra Tronca"
description: "Un'ombra vivente bidimensionale, legata a piani e superfici piane."
tier: "4"
ruolo: "Minion"
difficolta: "19"
hp: "1"
stress: "2"
soglia_danni: "Nessuna"
attacchi:
  - name: "Strangolamento"
    desc: "**+3** | Vicina | **10** magico"
tratti:
  - name: "Minion (12)"
    desc: "*- Passiva:* L'Ombra viene sconfitta quando subisce qualsiasi danno. Per ogni 12 danni che un PG infligge all'Ombra, il PG sconfigge un Minion aggiuntivo entro portata contro cui l'attacco avrebbe successo."
capacita_speciali:
  - name: "Aggancio dell'Ombra"
    desc: "*- Azione:* Segnare uno Stress per effettuare un attacco contro un bersaglio entro portata Vicina. In caso di successo, il bersaglio diventa *Vulnerabile* e deve segnare uno Stress quando compie un'azione finché l'Ombra non viene sconfitta."
  - name: "Attacco di Gruppo"
    desc: "*- Azione:* Spendere una Paura per scegliere un bersaglio e mettere a fuoco tutte le Ombre Tronche entro portata Vicina di esso. Quei Minion si muovono in portata Da Vicino del bersaglio ed effettuano un tiro d'attacco condiviso. In caso di successo, infliggono 10 danni magici ciascuno. Combina questi danni."
```
---
type:
  - "[[Creatura]]"
  - "[[Orda]]"
---

## Squadrone di Arceri
* **Descrizione:** Un gruppo di arcieri addestrati che impugnano archi massicci.
* **Tier:** 2 (Orda, 2/PF)
* **Difficoltà:** 13
* **Soglie di Danno:** 8/16
* **Punti Ferita:** 4 | **Stress:** 3
* **Attacchi:**
 * **Arco Lungo:** +0 | Lontana | 2d6+3 fisico
* **Tratti e Capacità:**
 * **Orda (1d6+3) - Passiva:** Quando il Squadrone ha segnato la metà o più dei propri PF, il loro attacco standard infligge **1d6+3** danni fisici invece.
 * **Volo Concentrato - Azione:** **Spendere uno Stress** per scegliere un punto in portata Lontana. Effettua un attacco con vantaggio contro tutti i bersagli in portata Vicina di quel punto. I bersagli colpiti subiscono **1d10+4** danni fisici.
 * **Fuoco Soppressivo - Azione:** **Segnare uno Stress** per scegliere un punto in portata Lontana. Fino al prossimo tiro con Stress, una creatura che si muove in portata Vicina di quel punto deve effettuare un Tiro di Reazione di Agilità. In caso di fallimento, subisce **2d6+3** danni fisici. In caso di successo, subisce metà danno.

```statblock
layout: DaggerHeart Nemici
name: "Squadrone di Arceri"
description: "Un gruppo di arcieri addestrati che impugnano archi massicci."
tier: "2"
ruolo: "Orda"
difficolta: "13"
hp: "4"
stress: "3"
soglia_danni: "8/16"
attacchi:
  - name: "Arco Lungo"
    desc: "**+0** | Lontana | **2d6+3** fisico"
tratti:
  - name: "Orda (1d6+3)"
    desc: "*- Passiva:* Quando il Squadrone ha segnato la metà o più dei propri PF, il loro attacco standard infligge 1d6+3 danni fisici invece."
capacita_speciali:
  - name: "Volo Concentrato"
    desc: "*- Azione:* Spendere uno Stress per scegliere un punto in portata Lontana. Effettua un attacco con vantaggio contro tutti i bersagli in portata Vicina di quel punto. I bersagli colpiti subiscono 1d10+4 danni fisici."
  - name: "Fuoco Soppressivo"
    desc: "*- Azione:* Segnare uno Stress per scegliere un punto in portata Lontana. Fino al prossimo tiro con Stress, una creatura che si muove in portata Vicina di quel punto deve effettuare un Tiro di Reazione di Agilità. In caso di fallimento, subisce 2d6+3 danni fisici. In caso di successo, subisce metà danno."
```
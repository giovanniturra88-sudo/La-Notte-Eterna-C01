---
type:
  - "[[Creatura]]"
  - "[[Minion]]"
---

## Mercenario
* **Descrizione:** Un mercenario armato che mette alla prova la propria fortuna.
* **Tier:** 1 (Minion)
* **Difficoltà:** 10
* **Soglie di Danno:** Nessuna
* **Punti Ferita:** 1 | **Stress:** 1
* **Attacchi:**
 * **Spada Lunga:** +3 | Da Vicino | 3 fisico
* **Tratti e Capacità:**
 * **Minion (4) - Passiva:** Il Mercenario è sconfitto quando riceve qualsiasi danno. Per ogni 4 danni che un PG infligge al Mercenario, sconfiggi un Minion aggiuntivo entro portata del colpo che avrebbe avuto successo.
 * **Attacco di Gruppo - Azione:** **Spendere una Paura** per scegliere un bersaglio e mettere a fuoco tutti i Mercenari in portata Da Vicino. Quei Minion si muovono in portata Da Vicino del bersaglio ed effettuano un colpo condiviso. In caso di successo, infliggono 3 danni fisici ciascuno. Combina questi danni.

```statblock
layout: DaggerHeart Nemici
name: "Mercenario"
description: "Un mercenario armato che mette alla prova la propria fortuna."
tier: "1"
ruolo: "Minion"
difficolta: "10"
hp: "1"
stress: "1"
soglia_danni: "Nessuna"
attacchi:
  - name: "Spada Lunga"
    desc: "**+3** | Da Vicino | **3** fisico"
tratti:
  - name: "Minion (4)"
    desc: "*- Passiva:* Il Mercenario è sconfitto quando riceve qualsiasi danno. Per ogni 4 danni che un PG infligge al Mercenario, sconfiggi un Minion aggiuntivo entro portata del colpo che avrebbe avuto successo."
capacita_speciali:
  - name: "Attacco di Gruppo"
    desc: "*- Azione:* Spendere una Paura per scegliere un bersaglio e mettere a fuoco tutti i Mercenari in portata Da Vicino. Quei Minion si muovono in portata Da Vicino del bersaglio ed effettuano un colpo condiviso. In caso di successo, infliggono 3 danni fisici ciascuno. Combina questi danni."
```
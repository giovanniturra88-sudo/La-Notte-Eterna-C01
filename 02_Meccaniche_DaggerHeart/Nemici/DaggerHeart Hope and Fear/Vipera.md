---
type:
  - "[[Creatura]]"
  - "[[Minion]]"
---

## Vipera
* **Descrizione:** Un piccolo serpente che avvelena la sua preda con zanne a cerniera.
* **Tier:** 1 (Minion)
* **Difficoltà:** 11
* **Soglie di Danno:** Nessuna
* **Punti Ferita:** 1 | **Stress:** 1
* **Esperienza:** Radicato +4
* **Attacchi:**
  * **Morso:** +3 | Da Vicino | 1 fisico
* **Tratti e Capacità:**
  * **Minion (4) - Passiva:** La Vipera viene sconfitta quando subisce qualsiasi danno. Per ogni 4 danni che un PG infligge alla Vipera, il PG sconfigge un Minion aggiuntivo entro la portata contro cui l'attacco avrebbe successo.
  * **Velenosa - Passiva:** Quando la Vipera effettua un attacco standard riuscito, il bersaglio diventa temporaneamente *Avvelenato*. Mentre è *Avvelenato*, il bersaglio deve segnare uno Stress ogni volta che effettua un tiro d'azione.
  * **Attacco di Gruppo - Azione:** Spendere una Paura per scegliere un bersaglio e mettere a fuoco tutte le Viper entro portata Vicina di esso. Quei Minion si muovono in portata Da Vicino del bersaglio ed effettuano un tiro d'attacco condiviso. In caso di successo, infliggono 1 danno fisico ciascuno. Combina questi danni.

```statblock
layout: DaggerHeart Nemici
name: "Vipera"
description: "Un piccolo serpente che avvelena la sua preda con zanne a cerniera."
tier: "1"
ruolo: "Minion"
difficolta: "11"
hp: "1"
stress: "1"
esperienza: "Radicato +4"
soglia_danni: "Nessuna"
attacchi:
  - name: "Morso"
    desc: "**+3** | Da Vicino | **1** fisico"
tratti:
  - name: "Minion (4)"
    desc: "*- Passiva:* La Vipera viene sconfitta quando subisce qualsiasi danno. Per ogni 4 danni che un PG infligge alla Vipera, il PG sconfigge un Minion aggiuntivo entro la portata contro cui l'attacco avrebbe successo."
  - name: "Velenosa"
    desc: "*- Passiva:* Quando la Vipera effettua un attacco standard riuscito, il bersaglio diventa temporaneamente Avvelenato. Mentre è Avvelenato, il bersaglio deve segnare uno Stress ogni volta che effettua un tiro d'azione."
capacita_speciali:
  - name: "Attacco di Gruppo"
    desc: "*- Azione:* Spendere una Paura per scegliere un bersaglio e mettere a fuoco tutte le Viper entro portata Vicina di esso. Quei Minion si muovono in portata Da Vicino del bersaglio ed effettuano un tiro d'attacco condiviso. In caso di successo, infliggono 1 danno fisico ciascuno. Combina questi danni."
```
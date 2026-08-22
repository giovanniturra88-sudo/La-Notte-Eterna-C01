---
type:
  - "[[Creatura]]"
  - "[[Minion]]"
---

## Rastrellatore Darkweave
* **Descrizione:** Un ragno delle dimensioni di una testa umana, tessuto con seta d'ombra.
* **Tier:** 1 (Minion)
* **Difficoltà:** 10
* **Soglie di Danno:** Nessuna
* **Punti Ferita:** 1 | **Stress:** 1
* **Esperienza:** Oscurità +3
* **Attacchi:**
  * **Morso:** -2 | Da Vicino | 2 fisico
* **Tratti e Capacità:**
  * **Minion (3) - Passiva:** Il Rastrellatore viene sconfitto quando subisce qualsiasi danno. Per ogni 3 danni che un PG infligge al Rastrellatore, il PG sconfigge un Minion aggiuntivo entro portata contro cui l'attacco avrebbe successo.
  * **Pelle Strisciante - Azione:** Spendere una Paura per costringere tutti i PG entro portata Da Vicino del Rastrellatore a segnare uno Stress.
  * **Attacco di Gruppo - Azione:** Spendere una Paura per scegliere un bersaglio e mettere a fuoco tutti i Rastrellatori Darkweave entro portata Vicina di esso. Quei Minion si muovono in portata Da Vicino del bersaglio ed effettuano un tiro d'attacco condiviso. In caso di successo, infliggono 2 danni fisici ciascuno. Combina questi danni.
  * **Veleno Darkweave - Reazione:** Quando il Rastrellatore effettua un attacco riuscito, puoi segnare uno Stress per *Esaurire* il bersaglio finché non riesce su un Tiro di Forza (9). Mentre è *Esaurito*, il bersaglio deve segnare uno Stress ogni volta che effettua un tiro di azione.

```statblock
layout: DaggerHeart Nemici
name: "Rastrellatore Darkweave"
description: "Un ragno delle dimensioni di una testa umana, tessuto con seta d'ombra."
tier: "1"
ruolo: "Minion"
difficolta: "10"
hp: "1"
stress: "1"
esperienza: "Oscurità +3"
soglia_danni: "Nessuna"
attacchi:
  - name: "Morso"
    desc: "**-2** | Da Vicino | **2** fisico"
capacita_speciali:
  - name: "Pelle Strisciante"
    desc: "*- Azione:* Spendere una Paura per costringere tutti i PG entro portata Da Vicino del Rastrellatore a segnare uno Stress."
  - name: "Attacco di Gruppo"
    desc: "*- Azione:* Spendere una Paura per scegliere un bersaglio e mettere a fuoco tutti i Rastrellatori Darkweave entro portata Vicina di esso. Quei Minion si muovono in portata Da Vicino del bersaglio ed effettuano un tiro d'attacco condiviso. In caso di successo, infliggono 2 danni fisici ciascuno. Combina questi danni."
  - name: "Veleno Darkweave"
    desc: "*- Reazione:* Quando il Rastrellatore effettua un attacco riuscito, puoi segnare uno Stress per *Esaurire* il bersaglio finché non riesce su un Tiro di Forza (9). Mentre è *Esaurito*, il bersaglio deve segnare uno Stress ogni volta che effettua un tiro di azione."
```
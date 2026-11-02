---
type:
  - "[[Creatura]]"
  - "[[Minion]]"
---

## Sprite
* **Descrizione:** Un minuscolo guerriero alato che attacca gli intrusi con frecce avvelenate.
* **Rango:** 2 (Minion)
* **Difficoltà:** 13
* **Soglie di Danno:** Nessuna
* **Punti Ferita:** 1 | **Stress:** 1
* **Esperienza:** Furtività +2, Vendetta +2
* **Attacchi:**
 * **Frecce Affilate come Aghi:** +0 | Ravvicinata | 5 fisico
* **Tratti e Capacità:**
 * **Minion (5) - Passiva:** Lo Sprite viene sconfitto quando subisce qualsiasi danno. Per ogni 5 danni che un PG infligge allo Sprite, il PG sconfigge un Minion aggiuntivo entro portata contro cui l'attacco avrebbe successo.
 * **Arte dell'Invisibilità - Azione:** Spendere una Paura per rendere lo Sprite *Nascosto* finché non attacca.
 * **Veleno del Fiore del Sogno - Azione:** Quando lo Sprite ha successo su un attacco standard, puoi spendere una Paura per rendere il bersaglio *Sonnecchioso* finché non subisce danni. Mentre è *Sonnecchioso*, il bersaglio deve effettuare un Tiro di Reazione di Presenza prima di effettuare un tiro d'azione. In caso di fallimento, deve segnare 2 Stress o addormentarsi finché non subisce danni.

```statblock
layout: DaggerHeart Nemici
name: "Sprite"
description: "Un minuscolo guerriero alato che attacca gli intrusi con frecce avvelenate."
tier: "2"
ruolo: "Minion"
difficolta: "13"
hp: "1"
stress: "1"
esperienza: "Furtività +2, Vendetta +2"
soglia_danni: "Nessuna"
attacchi:
  - name: "Frecce Affilate come Aghi"
    desc: "**+0** | Ravvicinata | **5** fisico"
tratti:
  - name: "Minion (5)"
    desc: "*- Passiva:* Lo Sprite viene sconfitto quando subisce qualsiasi danno. Per ogni 5 danni che un PG infligge allo Sprite, il PG sconfigge un Minion aggiuntivo entro portata contro cui l'attacco avrebbe successo."
capacita_speciali:
  - name: "Arte dell'Invisibilità"
    desc: "*- Azione:* Spendere una Paura per rendere lo Sprite *Nascosto* finché non attacca."
  - name: "Veleno del Fiore del Sogno"
    desc: "*- Azione:* Quando lo Sprite ha successo su un attacco standard, puoi spendere una Paura per rendere il bersaglio *Sonnecchioso* finché non subisce danni. Mentre è *Sonnecchioso*, il bersaglio deve effettuare un Tiro di Reazione di Presenza prima di effettuare un tiro d'azione. In caso di fallimento, deve segnare 2 Stress o addormentarsi finché non subisce danni."
```
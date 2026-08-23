---
type:
  - "[[Creatura]]"
  - "[[Solo]]"
---

## Scavatore Acido
* **Descrizione:** Un insetto grande come un cavallo con artigli scavatori e sangue acido.
* **Rango:** 1 (Solo)
* **Difficoltà:** 14
* **Soglie di Danno:** 8/15
* **Punti Ferita:** 8 | **Stress:** 3
* **Esperienza:** Sentiero Sismico +2
* **Attacchi:**
 * **Artigli:** +3 | Prossima | 1d12+2 fisico
* **Tratti e Capacità:**
 * **Inesorabile (3) - Passiva:** Lo Scavatore può essere messo a fuoco fino a tre volte per turno del GM. Spendere Paura come al solito per metterlo a fuoco.
 * **Eruzione Terrestre - Azione:** **Segnare uno Stress** per far sì che lo Scavatore esca dalla terra. Tutte le creature in portata Prossima devono superare un Tiro di Reazione di Agilità o essere rovesciate, rendendole _Vulnerabili_ fino al loro prossimo turno.
 * **Sputo d'Acido - Azione:** Effettua un attacco contro tutti i bersagli davanti allo Scavatore in portata Ravvicinata. I bersagli che falliscono l'attacco subiscono **2d6** danni fisici e devono segnare uno Slot di Armatura senza riceverne i benefici (possono comunque usare l'armatura per ridurre i danni). Se non possono segnare uno Slot di Armatura, devono segnare un PF aggiuntivo e tu guadagni una Paura.
 * **Bagnata d'Acido - Reazione:** Quando lo Scavatore subisce danni Gravi, tutte le creature in portata Ravvicinata vengono bagnate con il suo sangue acido, subendo **1d10** danni fisici. Questo getto copre il terreno in portata Prossima con sangue, e tutte le creature diverse dallo Scavatore che vi si muovono subiscono **1d6** danni fisici.

```statblock
layout: DaggerHeart Nemici
name: "Scavatore Acido"
description: "Un insetto grande come un cavallo con artigli scavatori e sangue acido."
tier: "1"
ruolo: "Solo"
difficolta: "14"
hp: "8"
stress: "3"
esperienza: "Sentiero Sismico +2"
soglia_danni: "8/15"
attacchi:
  - name: "Artigli"
    desc: "**+3** | Prossima | **1d12+2** fisico"
tratti:
  - name: "Inesorabile (3)"
    desc: "*- Passiva:* Lo Scavatore può essere messo a fuoco fino a tre volte per turno del GM. Spendere Paura come al solito per metterlo a fuoco."
capacita_speciali:
  - name: "Eruzione Terrestre"
    desc: "*- Azione:* Segnare uno Stress per far sì che lo Scavatore esca dalla terra. Tutte le creature in portata Prossima devono superare un Tiro di Reazione di Agilità o essere rovesciate, rendendole Vulnerabili fino al loro prossimo turno."
  - name: "Sputo d'Acido"
    desc: "*- Azione:* Effettua un attacco contro tutti i bersagli davanti allo Scavatore in portata Ravvicinata. I bersagli che falliscono l'attacco subiscono 2d6 danni fisici e devono segnare uno Slot di Armatura senza riceverne i benefici (possono comunque usare l'armatura per ridurre i danni). Se non possono segnare uno Slot di Armatura, devono segnare un PF aggiuntivo e tu guadagni una Paura."
  - name: "Bagnata d'Acido"
    desc: "*- Reazione:* Quando lo Scavatore subisce danni Gravi, tutte le creature in portata Ravvicinata vengono bagnate con il suo sangue acido, subendo 1d10 danni fisici. Questo getto copre il terreno in portata Prossima con sangue, e tutte le creature diverse dallo Scavatore che vi si muovono subiscono 1d6 danni fisici."
```
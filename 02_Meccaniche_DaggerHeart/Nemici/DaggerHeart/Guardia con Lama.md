---
type:
  - "[[Creatura]]"
  - "[[Standard]]"
---

## Guardia con Lama
* **Descrizione:** Una guardia corazzata che porta una spada e uno scudo dipinti con i colori della colonia.
* **Tier:** 1 (Standard)
* **Difficoltà:** 12
* **Soglie di Danno:** 5/9
* **Punti Ferita:** 5 | **Stress:** 2
* **Esperienza:** Conoscenza Locale +3
* **Attacchi:**
 * **Spada Lunga:** +1 | Da Vicino | 1d6+1 fisico
* **Tratti e Capacità:**
 * **Muro dello Scudo - Passiva:** Una creatura che cerca di muoversi entro portata Molto Vicina della Guardia deve superare un Tiro di Agilità. Se ci sono altre Guardie con Lama in fila accanto alla prima, e ciascuna è entro portata Da Vicino da un'altra guardia nella fila, la Difficoltà aumenta del numero totale di guardie in quella fila.
 * **Trattenere - Azione:** Effettua un attacco contro un bersaglio entro portata Molto Vicina. In caso di successo, **segnare uno Stress** per _Tenere Sotto Controllo_ il bersaglio fino a quando non si libera con un attacco riuscito, un Tiro di Finezza o un Tiro di Forza.

```statblock
layout: DaggerHeart Nemici
name: "Guardia con Lama"
description: "Una guardia corazzata che porta una spada e uno scudo dipinti con i colori della colonia."
tier: "1"
ruolo: "Standard"
difficolta: "12"
hp: "5"
stress: "2"
esperienza: "Conoscenza Locale +3"
soglia_danni: "5/9"
attacchi:
  - name: "Spada Lunga"
    desc: "**+1** | Da Vicino | **1d6+1** fisico"
tratti:
  - name: "Muro dello Scudo"
    desc: "*- Passiva:* Una creatura che cerca di muoversi entro portata Molto Vicina della Guardia deve superare un Tiro di Agilità. Se ci sono altre Guardie con Lama in fila accanto alla prima, e ciascuna è entro portata Da Vicino da un'altra guardia nella fila, la Difficoltà aumenta del numero totale di guardie in quella fila."
capacita_speciali:
  - name: "Trattenere"
    desc: "*- Azione:* Effettua un attacco contro un bersaglio entro portata Molto Vicina. In caso di successo, segnare uno Stress per Tenere Sotto Controllo il bersaglio fino a quando non si libera con un attacco riuscito, un Tiro di Finezza o un Tiro di Forza."
```
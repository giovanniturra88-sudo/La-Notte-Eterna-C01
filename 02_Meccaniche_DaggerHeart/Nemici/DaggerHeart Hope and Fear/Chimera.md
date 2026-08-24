---
type:
  - "[[Creatura]]"
  - "[[Picchiatore]]"
---

## Chimera
* **Descrizione:** Un mostro gigante che sputa fuoco, con la testa di un leone, il corpo di una capra e la coda di un serpente.
* **Rango:** 3 (Picchiatore)
* **Difficoltà:** 17
* **Soglie di Danno:** 22/40
* **Punti Ferita:** 9 | **Stress:** 5
* **Esperienza:** Predatore +3
* **Attacchi:**
 * **Artigli:** +5 | Ravvicinata | 3d12 fisico
* **Tratti e Capacità:**
 * **Mascelle Strazianti - Passiva:** Quando la Chimera effettua un attacco riuscito contro un PG, il bersaglio deve segnare 2 Casella Armatura per ridurre la gravità di una soglia.
 * **Doppio Artiglio - Azione:** Segnare uno Stress per effettuare due attacchi standard. Se entrambi gli attacchi riescono contro lo stesso bersaglio, combina i danni.
 * **Soffio di Fuoco - Azione:** Spendere una Paura per bersagliare fino a tre PG davanti alla Chimera entro portata Ravvicinata. Ogni bersaglio deve effettuare un Tiro di Reazione di Agilità (20). I bersagli che falliscono subiscono 3d12 danni magici. I bersagli che riescono devono scegliere di segnare una Casella Armatura o uno Stress.
 * **Colpo del Serpente - Reazione:** Quando un PG entro portata Ravvicinata bersaglia la Chimera con un attacco, puoi segnare uno Stress per attaccare il PG per primo. In caso di successo, infliggi 4d4+10 danni fisici e *Avvelena* il bersaglio finché non effettua il prossimo riposo o non riesce su un Tiro di Conoscenza (20). Mentre è *Avvelenato*, il bersaglio deve tirare un d6 prima di effettuare un tiro di azione. Con un risultato di 3 o inferiore, deve segnare uno Stress.

```statblock
layout: DaggerHeart Nemici
name: "Chimera"
description: "Un mostro gigante che sputa fuoco, con la testa di un leone, il corpo di una capra e la coda di un serpente."
tier: "3"
ruolo: "Picchiatore"
difficolta: "17"
hp: "9"
stress: "5"
esperienza: "Predatore +3"
soglia_danni: "22/40"
attacchi:
  - name: "Artigli"
    desc: "**+5** | Ravvicinata | **3d12** fisico"
tratti:
  - name: "Mascelle Strazianti"
    desc: "*- Passiva:* Quando la Chimera effettua un attacco riuscito contro un PG, il bersaglio deve segnare 2 Casella Armatura per ridurre la gravità di una soglia."
capacita_speciali:
  - name: "Doppio Artiglio"
    desc: "*- Azione:* Segnare uno Stress per effettuare due attacchi standard. Se entrambi gli attacchi riescono contro lo stesso bersaglio, combina i danni."
  - name: "Soffio di Fuoco"
    desc: "*- Azione:* Spendere una Paura per bersagliare fino a tre PG davanti alla Chimera entro portata Ravvicinata. Ogni bersaglio deve effettuare un Tiro di Reazione di Agilità (20). I bersagli che falliscono subiscono 3d12 danni magici. I bersagli che riescono devono scegliere di segnare una Casella Armatura o uno Stress."
  - name: "Colpo del Serpente"
    desc: "*- Reazione:* Quando un PG entro portata Ravvicinata bersaglia la Chimera con un attacco, puoi segnare uno Stress per attaccare il PG per primo. In caso di successo, infliggi 4d4+10 danni fisici e *Avvelena* il bersaglio finché non effettua il prossimo riposo o non riesce su un Tiro di Conoscenza (20). Mentre è *Avvelenato*, il bersaglio deve tirare un d6 prima di effettuare un tiro di azione. Con un risultato di 3 o inferiore, deve segnare uno Stress."
```
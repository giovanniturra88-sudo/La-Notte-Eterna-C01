---
type:
  - "[[Creatura]]"
  - "[[Solo]]"
aliases:
 - "Gargantuan War Machine"
---

## Macchina da Guerra Gargantuesca
* **Descrizione:** Un costrutto di adamantio alto 100 piedi, con occhi di gemme, alimentato da un crogiolo pettorale di fiamma elementale.
* **Rango:** 4 (Solo)
* **Difficoltà:** 20
* **Soglie di Danno:** 48/88
* **Punti Ferita:** 10 | **Stress:** 6
* **Esperienza:** Indistruttibile +3
* **Attacchi:**
 * **Pugni di Ferro:** +7 | Ravvicinata | 4d12+10 fisico
* **Tratti e Capacità:**
 * **Inesorabile (3) - Passiva:** La Macchina può essere messa a fuoco fino a tre volte per turno del GM. Spendere Paura come di consueto per metterla a fuoco.
 * **Dimensioni Imponenti - Passiva:** Quando la Macchina entra in campo di battaglia, ogni PG deve o perdere una Speranza o segnare 1d4 Stress.
 * **Pugno a Razzo - Azione:** Segnare uno Stress per effettuare un attacco contro un PG entro portata Ravvicinata. In caso di successo, il bersaglio subisce 4d12+10 danni fisici diretti e segna 2 Casella Armatura senza riceverne i benefici.
 * **Calpestio Frantumatore - Azione:** Spendere una Paura per scegliere un punto entro portata Ravvicinata ed effettuare un tiro d'attacco contro tutti i nemici entro portata Ravvicinata di quel punto. I bersagli contro cui l'attacco ha successo subiscono 4d12 danni fisici diretti e sono *Vulnerabili* finché non vengono messi a fuoco. Inoltre, l'intera area diventa macerie, e un PG deve superare un Tiro di Reazione di Agilità (16) per attraversarla.
 * **Sovraccarico - Reazione:** Conto alla rovescia (Loop 2d6). Quando la Macchina viene messa a fuoco per la prima volta, attiva il conto alla rovina. Si riduce ogni volta che la Macchina viene messa a fuoco. Quando scatta, posiziona un token su questo statblock mentre il crogiolo pettorale della Macchina si accende di fiamma magica. Per ogni token su questo statblock, la Macchina guadagna un bonus di +1 alla Difficoltà e ai tiri d'attacco, e il suo attacco standard infligge 1d12 danni aggiuntivi. Rimuovi un token quando la Macchina subisce danni Gravi.

```statblock
layout: DaggerHeart Nemici
name: "Macchina da Guerra Gargantuesca"
description: "Un costrutto di adamantio alto 100 piedi, con occhi di gemme, alimentato da un crogiolo pettorale di fiamma elementale."
tier: "4"
ruolo: "Solo"
difficolta: "20"
hp: "10"
stress: "6"
esperienza: "Indistruttibile +3"
soglia_danni: "48/88"
attacchi:
  - name: "Pugni di Ferro"
    desc: "**+7** | Ravvicinata | **4d12+10** fisico"
tratti:
  - name: "Inesorabile (3)"
    desc: "*- Passiva:* La Macchina può essere messa a fuoco fino a tre volte per turno del GM. Spendere Paura come di consueto per metterla a fuoco."
  - name: "Dimensioni Imponenti"
    desc: "*- Passiva:* Quando la Macchina entra in campo di battaglia, ogni PG deve o perdere una Speranza o segnare 1d4 Stress."
capacita_speciali:
  - name: "Pugno a Razzo"
    desc: "*- Azione:* Segnare uno Stress per effettuare un attacco contro un PG entro portata Ravvicinata. In caso di successo, il bersaglio subisce 4d12+10 danni fisici diretti e segna 2 Casella Armatura senza riceverne i benefici."
  - name: "Calpestio Frantumatore"
    desc: "*- Azione:* Spendere una Paura per scegliere un punto entro portata Ravvicinata ed effettuare un tiro d'attacco contro tutti i nemici entro portata Ravvicinata di quel punto. I bersagli contro cui l'attacco ha successo subiscono 4d12 danni fisici diretti e sono *Vulnerabili* finché non vengono messi a fuoco. Inoltre, l'intera area diventa macerie, e un PG deve superare un Tiro di Reazione di Agilità (16) per attraversarla."
  - name: "Sovraccarico"
    desc: "*- Reazione:* Conto alla rovescia (Loop 2d6). Quando la Macchina viene messa a fuoco per la prima volta, attiva il conto alla rovina. Si riduce ogni volta che la Macchina viene messa a fuoco. Quando scatta, posiziona un token su questo statblock mentre il crogiolo pettorale della Macchina si accende di fiamma magica. Per ogni token su questo statblock, la Macchina guadagna un bonus di +1 alla Difficoltà e ai tiri d'attacco, e il suo attacco standard infligge 1d12 danni aggiuntivi. Rimuovi un token quando la Macchina subisce danni Gravi."
```
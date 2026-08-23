---
type:
  - "[[Creatura]]"
  - "[[Furtivo]]"
---

## Aquila Gigante
* **Descrizione:** Un grande uccello di preda con artigli insanguinati.
* **Tier:** 2 (Furtivo)
* **Difficoltà:** 14
* **Soglie di Danno:** 8/19
* **Punti Ferita:** 4 | **Stress:** 4
* **Attacchi:**
 * **Artigli e Becco:** +1 | Molto Vicina | 2d6+3 fisico
* **Tratti e Capacità:**
 * **Volo - Passiva:** Mentre vola, l'Aquila guadagna un bonus di +3 alla propria Difficoltà.
 * **Attacco dal Cielo - Azione:** **Segnare uno Stress** per attaccare un bersaglio entro portata Lontana. In caso di successo, infliggi **2d10+2** danni fisici e colpisci il bersaglio facendolo cadere, rendendolo _Vulnerabile_ fino al suo prossimo turno.
 * **Decollo - Azione:** Effettua un attacco contro un bersaglio entro portata Molto Vicina. In caso di successo, infliggi **2d4+3** danni fisici e il bersaglio deve superare un Tiro di Reazione di Agilità o diventare temporaneamente _Ristretto_ tra gli enormi artigli dell'Aquila. Se il bersaglio è _Ristretto_, l'Aquila si solleva immediatamente in aria fino a portata Molto Lontana sopra il campo di battaglia mentre lo tiene.
 * **Lancio Mortale - Azione:** Mentre vola, l'Aquila può lasciar cadere un bersaglio _Ristretto_ che sta tenendo. Quando viene lasciato cadere, il bersaglio non è più _Ristretto_, ma inizia a cadere. Se la caduta non viene impedita durante l'azione successiva dei PG, il bersaglio subisce **2d20** danni fisici al momento dell'atterraggio.

```statblock
layout: DaggerHeart Nemici
name: "Aquila Gigante"
description: "Un grande uccello di preda con artigli insanguinati."
tier: "2"
ruolo: "Furtivo"
difficolta: "14"
hp: "4"
stress: "4"
soglia_danni: "8/19"
attacchi:
  - name: "Artigli e Becco"
    desc: "**+1** | Molto Vicina | **2d6+3** fisico"
tratti:
  - name: "Volo"
    desc: "*- Passiva:* Mentre vola, l'Aquila guadagna un bonus di +3 alla propria Difficoltà."
capacita_speciali:
  - name: "Attacco dal Cielo"
    desc: "*- Azione:* Segnare uno Stress per attaccare un bersaglio entro portata Lontana. In caso di successo, infliggi 2d10+2 danni fisici e colpisci il bersaglio facendolo cadere, rendendolo Vulnerabile fino al suo prossimo turno."
  - name: "Decollo"
    desc: "*- Azione:* Effettua un attacco contro un bersaglio entro portata Molto Vicina. In caso di successo, infliggi 2d4+3 danni fisici e il bersaglio deve superare un Tiro di Reazione di Agilità o diventare temporaneamente Ristretto tra gli enormi artigli dell'Aquila. Se il bersaglio è Ristretto, l'Aquila si solleva immediatamente in aria fino a portata Molto Lontana sopra il campo di battaglia mentre lo tiene."
  - name: "Lancio Mortale"
    desc: "*- Azione:* Mentre vola, l'Aquila può lasciar cadere un bersaglio Ristretto che sta tenendo. Quando viene lasciato cadere, il bersaglio non è più Ristretto, ma inizia a cadere. Se la caduta non viene impedita durante l'azione successiva dei PG, il bersaglio subisce 2d20 danni fisici al momento dell'atterraggio."
```
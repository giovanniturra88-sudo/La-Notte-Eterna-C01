---
type:
  - "[[Creatura]]"
  - "[[Solo]]"
---

## Drago Vulcanico Flagello Fuso
* **Descrizione:** Infuriato dalle proprie ferite, il drago esplode in lava fusa.
* **Rango:** 4 (Solo)
* **Difficoltà:** 20
* **Soglie di Danno:** 30/58
* **Punti Ferita:** 7 | **Stress:** 5
* **Esperienza:** Caccia dall'Alto +5
* **Attacchi:**
 * **Artigli Ricoperti di Lava:** +9 | Ravvicinata | 4d12+4 fisico
* **Tratti e Capacità:**
 * **Inesorabile (3) - Passiva:** Il Flagello Fuso può essere messo a fuoco fino a tre volte per turno del GM. Spendere Paura come al solito per metterlo a fuoco.
 * **Scaglie Spezzate - Passiva:** Quando il Flagello Fuso subisce danni, lancia un numero di **d6** pari ai PF segnati. Per ogni risultato uguale o superiore a 4, guadagni una Paura.
 * **Forza Frantumante - Azione:** **Segnare uno Stress** per effettuare un attacco contro un bersaglio entro portata Prossima. In caso di successo, il bersaglio subisce **4d8+1** danni fisici, perde una Speranza e viene spinto a portata Ravvicinata. Il Flagello Fuso elimina uno Stress.
 * **Eruzione - Azione:** **Spendere una Paura** per eruttare lava dal sottosuolo delle scaglie del Flagello Fuso, riempiendo l'area entro portata Prossima con lava fusa. Tutti i bersagli in quell'area devono superare un Tiro di Reazione di Agilità o subire **4d6+6** danni fisici e essere spinti a portata Ravvicinata. Questa area rimane lava. Quando una creatura diversa dal Flagello Fuso entra in quell'area o agisce mentre è all'interno, deve segnare 6 PF.
 * **Respiro Vulcanico - Reazione:** Quando il Flagello Fuso subisce danni Gravi, lancia un **d10**. Su un risultato di 8 o più, il Flagello Fuso soffia una corrente di lava davanti a sé entro portata Lontana. Tutti i bersagli in quell'area devono effettuare un Tiro di Reazione di Agilità. Chi fallisce subisce **2d10+4** danni fisici, segna **1d4 Stress** e diventa _Vulnerabile_ fino a quando non elimina uno Stress. Chi riesce subisce metà danni e deve segnare uno Stress.
 * **Schizzo di Lava - Reazione:** Quando il Flagello Fuso subisce danni Gravi da un attacco entro portata Prossima, il sangue fuso esce dalla ferita e infligge **2d10+4** danni fisici diretti all'attaccante.
 * **Vendetta Cinerea (Cambio di Fase) - Reazione:** Quando il Flagello Fuso segna l'ultimo PF, sostituiscilo con il Tiranno Cinereo e mettilo immediatamente a fuoco.

```statblock
layout: DaggerHeart Nemici
name: "Drago Vulcanico Flagello Fuso"
description: "Infuriato dalle proprie ferite, il drago esplode in lava fusa."
tier: "4"
ruolo: "Solo"
difficolta: "20"
hp: "7"
stress: "5"
esperienza: "Caccia dall'Alto +5"
soglia_danni: "30/58"
attacchi:
  - name: "Artigli Ricoperti di Lava"
    desc: "**+9** | Ravvicinata | **4d12+4** fisico"
tratti:
  - name: "Inesorabile (3)"
    desc: "*- Passiva:* Il Flagello Fuso può essere messo a fuoco fino a tre volte per turno del GM. Spendere Paura come al solito per metterlo a fuoco."
  - name: "Scaglie Spezzate"
    desc: "*- Passiva:* Quando il Flagello Fuso subisce danni, lancia un numero di d6 pari ai PF segnati. Per ogni risultato uguale o superiore a 4, guadagni una Paura."
capacita_speciali:
  - name: "Forza Frantumante"
    desc: "*- Azione:* Segnare uno Stress per effettuare un attacco contro un bersaglio entro portata Prossima. In caso di successo, il bersaglio subisce 4d8+1 danni fisici, perde una Speranza e viene spinto a portata Ravvicinata. Il Flagello Fuso elimina uno Stress."
  - name: "Eruzione"
    desc: "*- Azione:* Spendere una Paura per eruttare lava dal sottosuolo delle scaglie del Flagello Fuso, riempiendo l'area entro portata Prossima con lava fusa. Tutti i bersagli in quell'area devono superare un Tiro di Reazione di Agilità o subire 4d6+6 danni fisici e essere spinti a portata Ravvicinata. Questa area rimane lava. Quando una creatura diversa dal Flagello Fuso entra in quell'area o agisce mentre è all'interno, deve segnare 6 PF."
  - name: "Respiro Vulcanico"
    desc: "*- Reazione:* Quando il Flagello Fuso subisce danni Gravi, lancia un d10. Su un risultato di 8 o più, il Flagello Fuso soffia una corrente di lava davanti a sé entro portata Lontana. Tutti i bersagli in quell'area devono effettuare un Tiro di Reazione di Agilità. Chi fallisce subisce 2d10+4 danni fisici, segna 1d4 Stress e diventa Vulnerabile fino a quando non elimina uno Stress. Chi riesce subisce metà danni e deve segnare uno Stress."
  - name: "Schizzo di Lava"
    desc: "*- Reazione:* Quando il Flagello Fuso subisce danni Gravi da un attacco entro portata Prossima, il sangue fuso esce dalla ferita e infligge 2d10+4 danni fisici diretti all'attaccante."
  - name: "Vendetta Cinerea (Cambio di Fase)"
    desc: "*- Reazione:* Quando il Flagello Fuso segna l'ultimo PF, sostituiscilo con il Tiranno Cinereo e mettilo immediatamente a fuoco."
```
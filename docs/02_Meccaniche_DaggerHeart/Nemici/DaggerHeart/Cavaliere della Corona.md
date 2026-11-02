---
type:
  - "[[Creatura]]"
  - "[[Capo]]"
---

## Cavaliere della Corona
* **Descrizione:** Un soldato decorato con armatura pesante e un potente destriero.
* **Rango:** 2 (Capo)
* **Difficoltà:** 15
* **Soglie di Danno:** 13/26
* **Punti Ferita:** 6 | **Stress:** 4
* **Esperienza:** Conoscenza Antica +3, Alta Società +2, Tattiche +2
* **Attacchi:**
 * **Spada Lunga:** +4 | Ravvicinata | 2d10+4 fisico
* **Tratti e Capacità:**
 * **Chevalier - Passiva:** Mentre il Cavaliere è in sella, ottiene un bonus di +2 alla propria Difficoltà. Quando subisce danni Gravi, viene gettato dalla sua montura e perde questo vantaggio fino a quando non viene nuovamente messo a fuoco.
 * **Pesantemente Armato - Passiva:** Quando il Cavaliere subisce danni fisici, ridurli di 3.
 * **Carica di Cavalleria - Azione:** Se il Cavaliere è in sella, si muove fino a portata Lontana ed effettua un attacco standard contro un bersaglio. In caso di successo, infligge **2d8+4** danni fisici e il bersaglio deve segnare uno Stress.
 * **Per la Corona! - Azione:** **Segnare uno Stress** per mettere a fuoco **1d4+1** alleati. Gli attacchi che effettuano mentre sono a fuoco in questo modo infliggono danni ridotti alla metà.

```statblock
layout: DaggerHeart Nemici
name: "Cavaliere della Corona"
description: "Un soldato decorato con armatura pesante e un potente destriero."
tier: "2"
ruolo: "Capo"
difficolta: "15"
hp: "6"
stress: "4"
esperienza: "Conoscenza Antica +3, Alta Società +2, Tattiche +2"
soglia_danni: "13/26"
attacchi:
  - name: "Spada Lunga"
    desc: "**+4** | Ravvicinata | **2d10+4** fisico"
tratti:
  - name: "Chevalier"
    desc: "*- Passiva:* Mentre il Cavaliere è in sella, ottiene un bonus di +2 alla propria Difficoltà. Quando subisce danni Gravi, viene gettato dalla sua montura e perde questo vantaggio fino a quando non viene nuovamente messo a fuoco."
  - name: "Pesantemente Armato"
    desc: "*- Passiva:* Quando il Cavaliere subisce danni fisici, ridurli di 3."
capacita_speciali:
  - name: "Carica di Cavalleria"
    desc: "*- Azione:* Se il Cavaliere è in sella, si muove fino a portata Lontana ed effettua un attacco standard contro un bersaglio. In caso di successo, infligge 2d8+4 danni fisici e il bersaglio deve segnare uno Stress."
  - name: "Per la Corona!"
    desc: "*- Azione:* Segnare uno Stress per mettere a fuoco 1d4+1 alleati. Gli attacchi che effettuano mentre sono a fuoco in questo modo infliggono danni ridotti alla metà."
```
---
type:
  - "[[Creatura]]"
  - "[[Solo]]"
---

## Trollo della Montagna
* **Descrizione:** Un gigante orribile nato da una roccia massiccia. Indossa armature rubate e una cintura di teste mozzate o teschi.
* **Tier:** 1 (Solo)
* **Difficoltà:** 14
* **Soglie di Danno:** 8/15
* **Punti Ferita:** 8 | **Stress:** 3
* **Esperienza:** Montagne +4
* **Attacchi:**
  * **Nodosa di Teschi:** +2 | Molto Vicina | 1d8+1 fisico
* **Tratti e Capacità:**
  * **Inesorabile (3) - Passiva:** Il Trollo può essere messo a fuoco fino a tre volte per turno del GM. Spendere Paura come di consueto per metterlo a fuoco.
  * **Armatura Rubata - Passiva: Conto alla Rovina.** Quando il combattimento inizia, attiva un conto alla rovina con un valore pari al numero di PG. Quando il Trollo subisce danni, riduci la gravità di una soglia, poi riduci il conto alla rovina. Quando scatta, il Trollo evolve (vedi "Trollo della Montagna Incazzato").
  * **Sferzata della Nodosa - Azione:** Segnare uno Stress per effettuare un attacco contro tutti i bersagli davanti al Trollo entro portata Molto Vicina. I bersagli contro cui il Trollo ha successo subiscono 2d8+2 danni fisici.
  * **Trollo della Montagna Incazzato - Evoluzione:** Il Trollo perde i tratti "Armatura Rubata" e "Sferzata della Nodosa", poi guadagna un bonus di +1 alla sua Difficoltà. Inoltre, guadagna il tratto "Doppia Sferzata" e sostituisce "Nodosa di Teschi" con il seguente attacco standard:
    * **Sferzata degli Artigli:** Molto Vicina | 1d10+3 fisico
    * **Doppia Sferzata - Azione:** Spendere una Paura per muoversi fino a portata Vicina ed effettuare due attacchi standard contro un bersaglio entro portata Da Vicino. Se entrambi gli attacchi hanno successo, combina i danni e il bersaglio perde una Speranza.

```statblock
layout: DaggerHeart Nemici
name: "Trollo della Montagna"
description: "Un gigante orribile nato da una roccia massiccia. Indossa armature rubate e una cintura di teste mozzate o teschi."
tier: "1"
ruolo: "Solo"
difficolta: "14"
hp: "8"
stress: "3"
esperienza: "Montagne +4"
soglia_danni: "8/15"
attacchi:
  - name: "Nodosa di Teschi"
    desc: "**+2** | Molto Vicina | **1d8+1** fisico"
tratti:
  - name: "Inesorabile (3)"
    desc: "*- Passiva:* Il Trollo può essere messo a fuoco fino a tre volte per turno del GM. Spendere Paura come di consueto per metterlo a fuoco."
  - name: "Armatura Rubata"
    desc: "*- Passiva: Conto alla Rovina.* Quando il combattimento inizia, attiva un conto alla rovina con un valore pari al numero di PG. Quando il Trollo subisce danni, riduci la gravità di una soglia, poi riduci il conto alla rovina. Quando scatta, il Trollo evolve (vedi 'Trollo della Montagna Incazzato')."
capacita_speciali:
  - name: "Sferzata della Nodosa"
    desc: "*- Azione:* Segnare uno Stress per effettuare un attacco contro tutti i bersagli davanti al Trollo entro portata Molto Vicina. I bersagli contro cui il Trollo ha successo subiscono 2d8+2 danni fisici."
  - name: "Trollo della Montagna Incazzato (Evoluzione)"
    desc: "*- Evoluzione:* Il Trollo perde i tratti 'Armatura Rubata' e 'Sferzata della Nodosa', poi guadagna un bonus di +1 alla sua Difficoltà. Inoltre, guadagna il tratto 'Doppia Sferzata' e sostituisce 'Nodosa di Teschi' con 'Sferzata degli Artigli' (Molto Vicina | 1d10+3 fisico)."
  - name: "Doppia Sferzata"
    desc: "*- Azione:* Spendere una Paura per muoversi fino a portata Vicina ed effettuare due attacchi standard contro un bersaglio entro portata Da Vicino. Se entrambi gli attacchi hanno successo, combina i danni e il bersaglio perde una Speranza."
```
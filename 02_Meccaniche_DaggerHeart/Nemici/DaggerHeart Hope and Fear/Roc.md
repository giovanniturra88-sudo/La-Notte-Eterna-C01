---
type:
  - "[[Creatura]]"
  - "[[Solo]]"
---

## Roc
* **Descrizione:** Un falco gigante che nidifica nelle montagne e scatena tempeste.
* **Rango:** 3 (Solo)
* **Difficoltà:** 18
* **Soglie di Danno:** 20/35
* **Punti Ferita:** 12 | **Stress:** 6
* **Esperienza:** Cime Scoscese +3
* **Attacchi:**
 * **Becco e Artigli:** +3 | Prossima | 3d12+8 fisico
* **Tratti e Capacità:**
 * **Inesorabile (3) - Passiva:** Il Roc può essere messo a fuoco fino a tre volte per turno del GM. Spendere Paura come di consueto per metterlo a fuoco.
 * **Uccello Predatore - Passiva:** Una volta per turno del GM, il Roc può muoversi fino a portata Remota prima o dopo di compiere un'azione.
 * **Ecco la Bomba - Azione:** Spendere una Paura per far scatenare al Roc una tempesta di fulmini e tuoni. Effettua un tiro d'attacco contro 1d4+1 bersagli entro portata Lontana. I bersagli contro cui il Roc ha successo subiscono 3d12 danni magici. Poi ogni bersaglio entro portata Lontana del Roc deve effettuare un Tiro di Reazione di Agilità (20). I bersagli che falliscono subiscono 3d8 danni fisici e vengono respinti in portata Ravvicinata. I bersagli che riescono devono segnare uno Stress.
 * **Pressione Schiacciante - Reazione:** Quando il Roc effettua un attacco standard riuscito, puoi segnare uno Stress per far schiacciare al Roc il bersaglio con i suoi artigli, costringendolo a segnare 1d4 Stress e *Rendendo Trattenuto* il bersaglio finché non supera un Tiro di Forza (20).
 * **Guardiano del Nido - Evoluzione:** Quando le uova del Roc sono minacciate, guadagna i seguenti tratti:
 * **Sdegnato - Passiva:** Il Roc guadagna un bonus di +2 alla sua Difficoltà e un bonus ai tiri sui danni pari al numero di Stress che ha segnato.
 * **Aurea Elettificante - Passiva:** Il Roc ha resistenza ai danni magici. I PG che falliscono un tiro entro portata Prossima devono spendere una Speranza o segnare 1d4 Stress.

```statblock
layout: DaggerHeart Nemici
name: "Roc"
description: "Un falco gigante che nidifica nelle montagne e scatena tempeste."
tier: "3"
ruolo: "Solo"
difficolta: "18"
hp: "12"
stress: "6"
esperienza: "Cime Scoscese +3"
soglia_danni: "20/35"
attacchi:
  - name: "Becco e Artigli"
    desc: "**+3** | Prossima | **3d12+8** fisico"
tratti:
  - name: "Inesorabile (3)"
    desc: "*- Passiva:* Il Roc può essere messo a fuoco fino a tre volte per turno del GM. Spendere Paura come di consueto per metterlo a fuoco."
  - name: "Uccello Predatore"
    desc: "*- Passiva:* Una volta per turno del GM, il Roc può muoversi fino a portata Remota prima o dopo di compiere un'azione."
capacita_speciali:
  - name: "Ecco la Bomba"
    desc: "*- Azione:* Spendere una Paura per far scatenare al Roc una tempesta di fulmini e tuoni. Effettua un tiro d'attacco contro 1d4+1 bersagli entro portata Lontana. I bersagli contro cui il Roc ha successo subiscono 3d12 danni magici. Poi ogni bersaglio entro portata Lontana del Roc deve effettuare un Tiro di Reazione di Agilità (20). I bersagli che falliscono subiscono 3d8 danni fisici e vengono respinti in portata Ravvicinata. I bersagli che riescono devono segnare uno Stress."
  - name: "Pressione Schiacciante"
    desc: "*- Reazione:* Quando il Roc effettua un attacco standard riuscito, puoi segnare uno Stress per far schiacciare al Roc il bersaglio con i suoi artigli, costringendolo a segnare 1d4 Stress e *Rendendo Trattenuto* il bersaglio finché non supera un Tiro di Forza (20)."
  - name: "Guardiano del Nido (Evoluzione)"
    desc: "*- Evoluzione:* Quando le uova del Roc sono minacciate, guadagna i tratti 'Sdegnato' e 'Aurea Elettificante'."
```
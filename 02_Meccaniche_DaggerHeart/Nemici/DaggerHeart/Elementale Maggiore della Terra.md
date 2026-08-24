---
type:
  - "[[Creatura]]"
  - "[[Picchiatore]]"
---

## Elementale Maggiore della Terra
* **Descrizione:** Una frana vivente di massi e polvere, grande come una casa.
* **Rango:** 3 (Picchiatore)
* **Difficoltà:** 17
* **Soglie di Danno:** 22/40
* **Punti Ferita:** 10 | **Stress:** 4
* **Attacchi:**
 * **Pugno di Masso:** +7 | Prossima | 3d10+1 fisico
* **Tratti e Capacità:**
 * **Lento - Passiva:** Quando metti a fuoco l'Elementale e non ha un gettone sul suo blocco statistiche, non può agire ancora. Posiziona un gettone sul suo blocco statistiche e descrivi cosa sta preparando di fare. Quando metti a fuoco l'Elementale e ha un gettone sul suo blocco statistiche, rimuovi il gettone e può agire.
 * **Colpi Schiaccianti - Passiva:** Quando l'Elementale effettua un attacco riuscito, la vittima deve segnare una Casella Armatura senza riceverne i benefici (può comunque usare l'armatura per ridurre il danno). Se non può segnare una Casella Armatura, deve segnare un PF aggiuntivo.
 * **Oggetto Immobile - Passiva:** Un attacco che sposterebbe l'Elementale lo sposta di due distanze in meno (ad esempio, Lontana diventa Prossima). Quando l'Elementale subisce danni fisici, riducili di 7.
 * **Frana - Azione:** **Segnare uno Stress** per creare una frana che seppellisce il terreno davanti all'Elementale entro portata Ravvicinata con caduta di rocce. Tutte le vittime in quest'area devono effettuare un Tiro di Reazione di Agilità (19). Le vittime che falliscono subiscono **2d12+5** danni fisici e diventano _Vulnerabili_ fino al loro prossimo tiro con Speranza. Le vittime che riescono subiscono metà danno.
 * **Impulso - Reazione:** Quando l'Elementale effettua un attacco riuscito contro un PG, guadagni una Paura.

```statblock
layout: DaggerHeart Nemici
name: "Elementale Maggiore della Terra"
description: "Una frana vivente di massi e polvere, grande come una casa."
tier: "3"
ruolo: "Picchiatore"
difficolta: "17"
hp: "10"
stress: "4"
soglia_danni: "22/40"
attacchi:
  - name: "Pugno di Masso"
    desc: "**+7** | Prossima | **3d10+1** fisico"
tratti:
  - name: "Lento"
    desc: "*- Passiva:* Quando metti a fuoco l'Elementale e non ha un gettone sul suo blocco statistiche, non può agire ancora. Posiziona un gettone sul suo blocco statistiche e descrivi cosa sta preparando di fare. Quando metti a fuoco l'Elementale e ha un gettone sul suo blocco statistiche, rimuovi il gettone e può agire."
  - name: "Colpi Schiaccianti"
    desc: "*- Passiva:* Quando l'Elementale effettua un attacco riuscito, la vittima deve segnare una Casella Armatura senza riceverne i benefici (può comunque usare l'armatura per ridurre il danno). Se non può segnare una Casella Armatura, deve segnare un PF aggiuntivo."
  - name: "Oggetto Immobile"
    desc: "*- Passiva:* Un attacco che sposterebbe l'Elementale lo sposta di due distanze in meno (ad esempio, Lontana diventa Prossima). Quando l'Elementale subisce danni fisici, riducili di 7."
capacita_speciali:
  - name: "Frana"
    desc: "*- Azione:* Segnare uno Stress per creare una frana che seppellisce il terreno davanti all'Elementale entro portata Ravvicinata con caduta di rocce. Tutte le vittime in quest'area devono effettuare un Tiro di Reazione di Agilità (19). Le vittime che falliscono subiscono 2d12+5 danni fisici e diventano Vulnerabili fino al loro prossimo tiro con Speranza. Le vittime che riescono subiscono metà danno."
  - name: "Impulso"
    desc: "*- Reazione:* Quando l'Elementale effettua un attacco riuscito contro un PG, guadagni una Paura."
```
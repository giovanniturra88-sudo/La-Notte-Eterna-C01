---
type:
  - "[[Creatura]]"
  - "[[Solo]]"
---

## Scatola da Battaglia
* **Descrizione:** Un costrutto a forma di cubo con una diversa runa su ognuna delle sue sei facce.
* **Rango:** 2 (Solo)
* **Difficoltà:** 15
* **Soglie di Danno:** 10/20
* **Punti Ferita:** 8 | **Stress:** 6
* **Esperienza:** Camuffamento +2
* **Attacchi:**
 * **Colpo:** +2 | Ravvicinata | 2d6+3 fisico
* **Tratti e Capacità:**
 * **Inesorabile (2) - Passiva:** La Scatola può essere messa a fuoco fino a due volte per turno del GM. Spendere Paura come al solito per metterla a fuoco.
 * **Tattiche Casuali - Azione:** **Segnare uno Stress** e lanciare un **d6**. La Scatola utilizza la mossa corrispondente:
 - 1. _Raggio di Mana._ La Scatola spara un raggio ardente. Effettua un attacco contro un bersaglio in portata Lontana. In caso di successo, infliggi **2d10+2** danni magici.
 - 2. _Jet di Fuoco._ La Scatola spara in aria, ruotando e rilasciando getti di fiamme. Effettua un attacco contro tutti i bersagli in portata Ravvicinata. I bersagli che falliscono l'attacco subiscono **2d8** danni fisici.
 - 3. _Travolgere._ La Scatola si muove in modo errante. Effettua un attacco contro tutti i PG in portata Ravvicinata. I bersagli che falliscono l'attacco subiscono **1d6+5** danni fisici e diventano _Vulnerabili_ fino al loro prossimo tiro con Speranza.
 - 4. _Gas Elettrico._ La Scatola sprigiona un gas argentato scintillante di fulmini. Tutti i bersagli in portata Ravvicinata devono superare un Tiro di Reazione di Agilità o segnare 3 Stress.
 - 5. _Battito Stordente._ La Scatola salta e le sue facce si schiacciano, creando una piccola esplosione sonora. Tutti i bersagli in portata Prossima devono superare un Tiro di Reazione di Forza o diventano _Vulnerabili_ fino alla sconfitta del cubo.
 - 6. _Lamento Psionico._ La Scatola rilascia una serie di api meccaniche il cui ronzio scuote le menti mortali. Tutti i bersagli in portata Ravvicinata devono superare un Tiro di Reazione di Presenza o subire **2d4+9** danni magici diretti.
 * **Sovraccarica - Reazione:** Prima di lanciare i danni per l'attacco della Scatola, puoi **segnare uno Stress** per aggiungere un **d6** al tiro di danno. Inoltre, guadagni una Paura.
 * **Terremoto della Morte - Reazione:** Quando la Scatola segna l'ultimo PF, la magia che lo alimenta esplode con forza. Tutti i bersagli in portata Ravvicinata devono superare un Tiro di Reazione di Istinto o subire **2d8+1** danni magici.

```statblock
layout: DaggerHeart Nemici
name: "Scatola da Battaglia"
description: "Un costrutto a forma di cubo con una diversa runa su ognuna delle sue sei facce."
tier: "2"
ruolo: "Solo"
difficolta: "15"
hp: "8"
stress: "6"
esperienza: "Camuffamento +2"
soglia_danni: "10/20"
attacchi:
  - name: "Colpo"
    desc: "**+2** | Ravvicinata | **2d6+3** fisico"
tratti:
  - name: "Inesorabile (2)"
    desc: "*- Passiva:* La Scatola può essere messa a fuoco fino a due volte per turno del GM. Spendere Paura come al solito per metterla a fuoco."
capacita_speciali:
  - name: "Tattiche Casuali"
    desc: "*- Azione:* Segnare uno Stress e lanciare un d6. La Scatola utilizza la mossa corrispondente: 1. Raggio di Mana - Effettua un attacco contro un bersaglio in portata Lontana. In caso di successo, infliggi 2d10+2 danni magici. 2. Jet di Fuoco - Effettua un attacco contro tutti i bersagli in portata Ravvicinata. I bersagli che falliscono l'attacco subiscono 2d8 danni fisici. 3. Travolgere - Effettua un attacco contro tutti i PG in portata Ravvicinata. I bersagli che falliscono l'attacco subiscono 1d6+5 danni fisici e diventano Vulnerabili fino al loro prossimo tiro con Speranza. 4. Gas Elettrico - Tutti i bersagli in portata Ravvicinata devono superare un Tiro di Reazione di Agilità o segnare 3 Stress. 5. Battito Stordente - Tutti i bersagli in portata Prossima devono superare un Tiro di Reazione di Forza o diventano Vulnerabili fino alla sconfitta del cubo. 6. Lamento Psionico - Tutti i bersagli in portata Ravvicinata devono superare un Tiro di Reazione di Presenza o subire 2d4+9 danni magici diretti."
  - name: "Sovraccarica"
    desc: "*- Reazione:* Prima di lanciare i danni per l'attacco della Scatola, puoi segnare uno Stress per aggiungere un d6 al tiro di danno. Inoltre, guadagni una Paura."
  - name: "Terremoto della Morte"
    desc: "*- Reazione:* Quando la Scatola segna l'ultimo PF, la magia che lo alimenta esplode con forza. Tutti i bersagli in portata Ravvicinata devono superare un Tiro di Reazione di Istinto o subire 2d8+1 danni magici."
```
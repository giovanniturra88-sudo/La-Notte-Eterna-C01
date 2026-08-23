---
type:
  - "[[Creatura]]"
  - "[[Solo]]"
aliases:
 - "Soul-Shattered Mage"
---

## Mago dall'Anima Sfrantumata
* **Descrizione:** Un incantatore la cui psiche è stata spezzata da una conoscenza che sarebbe meglio lasciare nascosta.
* **Tier:** 1 (Solo)
* **Difficoltà:** 12
* **Soglie di Danno:** 8/15
* **Punti Ferita:** 6 | **Stress:** 5
* **Esperienza:** Conoscenza Divietata +2
* **Attacchi:**
 * **Bastone di Assenzio:** +2 | Lontana | 1d12 magico
* **Tratti e Capacità:**
 * **Inesorabile (3) - Passiva:** Il Mago può essere messo a fuoco fino a tre volte per turno del GM. Spendere Paura come di consueto per metterlo a fuoco.
 * **Magia Spezzata - Azione:** Segnare uno Stress per tirare un d6. Il Mago usa la mossa corrispondente:
 * **1-2: Fessura Dimensionale.** Scegli un bersaglio entro portata Lontana. Il bersaglio teletrasporta a un punto che scegli entro portata Vicina della sua posizione originale e subisce 2d6 danni magici diretti mentre corpo e mente si riassemblano.
 * **3-4: Dilatazione del Tempo.** Scegli un gruppo di PG entro portata Lontana. Ogni bersaglio è *Rallentato* finché non tira con Speranza. Mentre è *Rallentato*, un bersaglio è *Vulnerabile* e deve segnare uno Stress quando si muove.
 * **5-6: Visioni Discordanti.** Effettua un attacco contro fino a tre bersagli entro portata Vicina. I bersagli contro cui il Mago ha successo subiscono 2d8 danni magici diretti.
 * **Senti il Mio Dolore - Reazione:** Quando il Mago segna PF, tira un numero di d6 pari al numero di Stress che il Mago ha segnato. Il Mago infligge danni magici diretti pari al risultato totale a tutti i PG entro portata Molto Vicina.

```statblock
layout: DaggerHeart Nemici
name: "Mago dall'Anima Sfrantumata"
description: "Un incantatore la cui psiche è stata spezzata da una conoscenza che sarebbe meglio lasciare nascosta."
tier: "1"
ruolo: "Solo"
difficolta: "12"
hp: "6"
stress: "5"
esperienza: "Conoscenza Divietata +2"
soglia_danni: "8/15"
attacchi:
  - name: "Bastone di Assenzio"
    desc: "**+2** | Lontana | **1d12** magico"
tratti:
  - name: "Inesorabile (3)"
    desc: "*- Passiva:* Il Mago può essere messo a fuoco fino a tre volte per turno del GM. Spendere Paura come di consueto per metterlo a fuoco."
capacita_speciali:
  - name: "Magia Spezzata"
    desc: "*- Azione:* Segnare uno Stress per tirare un d6. Il Mago usa la mossa corrispondente: 1-2 Fessura Dimensionale. 3-4 Dilatazione del Tempo. 5-6 Visioni Discordanti (vedi descrizione completa nel corpo del file)."
  - name: "Senti il Mio Dolore"
    desc: "*- Reazione:* Quando il Mago segna PF, tira un numero di d6 pari al numero di Stress che il Mago ha segnato. Il Mago infligge danni magici diretti pari al risultato totale a tutti i PG entro portata Molto Vicina."
```
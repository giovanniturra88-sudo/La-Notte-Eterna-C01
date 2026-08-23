---
type:
  - "[[Creatura]]"
  - "[[Solo]]"
---

## Idra
* **Descrizione:** Una bestia a quattro zampe ricoperta di squame con più teste lunghe, ciascuna piena di terrificanti zanne.
* **Tier:** 3 (Solo)
* **Difficoltà:** 18
* **Soglie di Danno:** 19/35
* **Punti Ferita:** 10 | **Stress:** 5
* **Attacchi:**
 * **Morso:** +3 | Da Vicino | 2d12+2 fisico
* **Tratti e Capacità:**
 * **Minaccia a Teste Multiple - Passiva:** L'Idra inizia con tre teste e ne può avere fino a cinque. Quando l'Idra subisce danni Gravi o maggiori, perde una testa.
 * **Inesorabile (X) - Passiva:** L'Idra può essere messa a fuoco X volte per turno del GM, dove X è il numero di teste dell'Idra. Spendere Paura normalmente per metterla a fuoco.
 * **Rigenerazione - Azione:** Se l'Idra ha dei PF segnati, **Spendere una Paura** per rimuovere un PF e farne crescere due.
 * **Coro Terrificante - Azione:** Tutti i PG in portata Lontana perdono 2 Speranza.
 * **Debolezza Magica - Reazione:** Quando l'Idra subisce danni magici, diventa _Confusa_ fino al prossimo tiro con Paura. Mentre è _Confusa_, non può usare la sua azione di Rigenerazione ma è immune ai danni magici.

```statblock
layout: DaggerHeart Nemici
name: "Idra"
description: "Una bestia a quattro zampe ricoperta di squame con più teste lunghe, ciascuna piena di terrificanti zanne."
tier: "3"
ruolo: "Solo"
difficolta: "18"
hp: "10"
stress: "5"
soglia_danni: "19/35"
attacchi:
  - name: "Morso"
    desc: "**+3** | Da Vicino | **2d12+2** fisico"
tratti:
  - name: "Minaccia a Teste Multiple"
    desc: "*- Passiva:* L'Idra inizia con tre teste e ne può avere fino a cinque. Quando l'Idra subisce danni Gravi o maggiori, perde una testa."
  - name: "Inesorabile (X)"
    desc: "*- Passiva:* L'Idra può essere messa a fuoco X volte per turno del GM, dove X è il numero di teste dell'Idra. Spendere Paura normalmente per metterla a fuoco."
capacita_speciali:
  - name: "Rigenerazione"
    desc: "*- Azione:* Se l'Idra ha dei PF segnati, Spendere una Paura per rimuovere un PF e farne crescere due."
  - name: "Coro Terrificante"
    desc: "*- Azione:* Tutti i PG in portata Lontana perdono 2 Speranza."
  - name: "Debolezza Magica"
    desc: "*- Reazione:* Quando l'Idra subisce danni magici, diventa Confusa fino al prossimo tiro con Paura. Mentre è Confusa, non può usare la sua azione di Rigenerazione ma è immune ai danni magici."
```
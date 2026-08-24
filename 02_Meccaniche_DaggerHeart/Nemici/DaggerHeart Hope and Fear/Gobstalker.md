---
type:
  - "[[Creatura]]"
  - "[[Solo]]"
---

## Gobstalker
* **Descrizione:** Una sfera carnosa e fluttuante di denti, con numerosi occhi e un fascio di tentacoli orali esploratori che scagliano raggi magici.
* **Rango:** 2 (Solo)
* **Difficoltà:** 15
* **Soglie di Danno:** 10/20
* **Punti Ferita:** 8 | **Stress:** 6
* **Esperienza:** Magia +3
* **Attacchi:**
 * **Tentacoli Orali:** +2 | Prossima | 2d6+3 fisico
* **Tratti e Capacità:**
 * **Inesorabile (3) - Passiva:** Il Gobstalker può essere messo a fuoco fino a tre volte per turno del GM. Spendere Paura come di consueto per metterlo a fuoco.
 * **Alitosi Anti-Mistica - Passiva:** L'alito fetido del Gobstalker crea una miasma invisibile che annulla la magia. Un attacco, un'abilità o un incantesimo che infligge danni magici o crea un effetto magico fallisce automaticamente se usato entro portata Ravvicinata del Gobstalker.
 * **Raggi dei Tentacoli - Azione:** Segnare uno Stress per attaccare un bersaglio entro portata Lontana. In caso di successo, tira un d8 per un attacco a raggio casuale o spendere una Paura per sceglierlo:
 1. **Affascina.** Il Gobstalker *Affascina* il bersaglio. Mentre è *Affascinato*, il bersaglio vede il Gobstalker come un amico e non può attaccarlo. Inoltre, quando un PG tira con Paura, un PG *Affascinato* deve segnare uno Stress o attaccare un bersaglio scelto dal Gobstalker. Un PG *Affascinato* deve superare un Tiro di Istitinto (16) per rimuovere la condizione.
 2. **Corrode.** Il bersaglio subisce 2d8 danni magici e deve segnare una Casella Armatura senza riceverne i benefici (può comunque usare l'armatura per ridurre i danni). Se non può, raddoppia i danni.
 3. **Rovina.** Il bersaglio deve segnare tutti i PF, ma può spendere un numero qualsiasi di Speranze per ridurre il numero di PF segnati in questo modo di un importo pari.
 4. **Ipnosi.** Il bersaglio cade in una *Trance Profonda* e non può agire se non per cercare di svegliarsi. Questa condizione dura finché il bersaglio subisce danni o si sveglia con un Tiro di Presenza riuscito (16).
 5. **Paralizza.** Il bersaglio si gela sul posto, diventando *Vulnerabile* e *Trattenuto* finché non segna 2 Stress.
 6. **Brucia.** Il bersaglio subisce 2d8 danni magici diretti.
 7. **Spaventa.** Il bersaglio è *Spaventato*. Mentre è *Spaventato*, il bersaglio non può compiere azioni diverse dalla fuga dalla battaglia o dal tentativo di scrollarsi di dosso il terrore. Inoltre, il bersaglio deve segnare uno Stress ogni volta che spendi una Paura. Il bersaglio può rimuovere la condizione con un Tiro di Presenza riuscito (16).
 8. **Rallenta.** Il bersaglio diventa *Vulnerabile* e deve segnare uno Stress per muoversi finché non spende 2 Speranze.
 * **Leccata della Sanguisuga - Reazione:** In caso di attacco standard riuscito, puoi spendere una Paura per rimuovere un numero di Stress pari al numero di PF segnati dal bersaglio.

```statblock
layout: DaggerHeart Nemici
name: "Gobstalker"
description: "Una sfera carnosa e fluttuante di denti, con numerosi occhi e un fascio di tentacoli orali esploratori che scagliano raggi magici."
tier: "2"
ruolo: "Solo"
difficolta: "15"
hp: "8"
stress: "6"
esperienza: "Magia +3"
soglia_danni: "10/20"
attacchi:
  - name: "Tentacoli Orali"
    desc: "**+2** | Prossima | **2d6+3** fisico"
tratti:
  - name: "Inesorabile (3)"
    desc: "*- Passiva:* Il Gobstalker può essere messo a fuoco fino a tre volte per turno del GM. Spendere Paura come di consueto per metterlo a fuoco."
  - name: "Alitosi Anti-Mistica"
    desc: "*- Passiva:* L'alito fetido del Gobstalker crea una miasma invisibile che annulla la magia. Un attacco, un'abilità o un incantesimo che infligge danni magici o crea un effetto magico fallisce automaticamente se usato entro portata Ravvicinata del Gobstalker."
capacita_speciali:
  - name: "Raggi dei Tentacoli"
    desc: "*- Azione:* Segnare uno Stress per attaccare un bersaglio entro portata Lontana. In caso di successo, tira un d8 per un attacco a raggio casuale o spendere una Paura per sceglierlo: 1. Affascina. 2. Corrode. 3. Rovina. 4. Ipnosi. 5. Paralizza. 6. Brucia. 7. Spaventa. 8. Rallenta (vedi descrizione completa nel corpo del file)."
  - name: "Leccata della Sanguisuga"
    desc: "*- Reazione:* In caso di attacco standard riuscito, puoi spendere una Paura per rimuovere un numero di Stress pari al numero di PF segnati dal bersaglio."
```
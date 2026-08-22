import os
import re

# ============================================================
# Translations for DaggerHeart folder
# filename -> (translated_title, translated_description)
# ============================================================
daggerheart_translations = {
    'Attune Relic.md': ('Reliquia di Sintonia', 'Ottieni un bonus di +1 alla tua Istinto. Puoi trasportare una sola reliquia.'),
    'Control Relic.md': ('Reliquia di Controllo', 'Ottieni un bonus di +1 alla tua Finezza. Puoi trasportare una sola reliquia.'),
    'Elusive Amulet.md': ('Amuleto Elusivo', 'Una volta per riposo lungo, puoi attivare questo amuleto per diventare Nascosto finché non ti muovi. Mentre sei Nascosto in questo modo, rimani invisibile anche se un avversario si muove dove normalmente ti vedrebbe.'),
    'Empty Chest.md': ('Cassa Vuota', 'Questa cassa magica sembra vuota. Quando pronunci una parola o un\'azione innescante specifica e apri la cassa, puoi vedere gli oggetti conservati al suo interno.'),
    'Enlighten Relic.md': ('Reliquia di Illuminazione', 'Ottieni un bonus di +1 alla tua Conoscenza. Puoi trasportare una sola reliquia.'),
    'Fire Jar.md': ('Barattolo di Fuoco', 'Puoi versare lo strano contenuto liquido di questo barattolo per produrre immediatamente fuoco. Il contenuto si rigenera quando effettui un riposo lungo.'),
    'Flickerfly Pendant.md': ('Ciondolo della Farfalla Tremula', 'Mentre porti questo ciondolo, le tue armi con gittata da Mischia che infliggono danni fisici hanno una lucentezza di filo di ragno e possono attaccare bersagli entro gittata Molto Vicina.'),
    'Gem of Alacrity.md': ('Gemma di Rapidità', 'Puoi fissare questa gemma a un\'arma, permettendoti di usare la tua Agilità quando effettui un attacco con quell\'arma.'),
    'Gem of Audacity.md': ('Gemma di Audacia', 'Puoi fissare questa gemma a un\'arma, permettendoti di usare la tua Presenza quando effettui un attacco con quell\'arma.'),
    'Gem of Insight.md': ('Gemma di Intuizione', 'Puoi fissare questa gemma a un\'arma, permettendoti di usare la tua Istinto quando effettui un attacco con quell\'arma.'),
    'Gem of Might.md': ('Gemma di Possanza', 'Puoi fissare questa gemma a un\'arma, permettendoti di usare la tua Forza quando effettui un attacco con quell\'arma.'),
    'Gem of Precision.md': ('Gemma di Precisione', 'Puoi fissare questa gemma a un\'arma, permettendoti di usare la tua Finezza quando effettui un attacco con quell\'arma.'),
    'Gem of Sagacity.md': ('Gemma di Saggezza', 'Puoi fissare questa gemma a un\'arma, permettendoti di usare la tua Conoscenza quando effettui un attacco con quell\'arma.'),
    'Glamour Stone.md': ('Pietra di Glamour', 'Attiva questa pietra delle dimensioni di un sassolino per memorizzare l\'aspetto di qualcuno che puoi vedere. Spendi una Speranza per ricreare magicamente questa parvenza su di te come illusione.'),
    'Glider.md': ('Aliante', 'Mentre cadi, puoi segnare uno Stress per dispiegare questo piccolo paracadute e planare al suolo in sicurezza.'),
    'Greatstone.md': ('Grande Pietra', 'Puoi fissare questa pietra a un\'arma che non ha già una caratteristica. L\'arma ottiene la seguente caratteristica. Potente: Con un attacco riuscito, tira un dado di danno aggiuntivo e scarta il risultato più basso.'),
    'Honing Relic.md': ('Reliquia di Affilatura', 'Ottieni un bonus di +1 a un\'Esperienza di tua scelta. Puoi trasportare una sola reliquia.'),
    'Hopekeeper Locket.md': ('Medaglione del Custode della Speranza', 'Durante un riposo lungo, se hai 6 Speranza, puoi spendere una Speranza per infondere questo medaglione con la tua generosa determinazione. Quando hai 0 Speranza, puoi usare il medaglione per guadagnare immediatamente una Speranza. Il medaglione deve essere re-infuso prima di poter essere usato di nuovo in questo modo.'),
    'Infinite Bag.md': ('Sacca Infinita', 'Quando conservi oggetti in questa sacca, vengono custoditi in una dimensione tascabile che non finisce mai lo spazio. Puoi recuperare un oggetto in qualsiasi momento.'),
    'Lakestrider Boots.md': ('Stivali del Camminatore del Lago', 'Puoi camminare sulla superficie dell\'acqua come se fosse terreno morbido.'),
    'Lorekeeper.md': ('Custode del Sapere', 'Puoi conservare il nome e i dettagli di fino a tre creature ostili all\'interno di questo libro. Ottieni un bonus di +1 ai tiri di azione contro quelle creature.'),
    'Manacles.md': ('Manette', 'Questo paio di manette con serratura viene fornito con una chiave.'),
    'Minor Health Potion Recipe.md': ('Ricetta: Pozione di Salute Minore', 'Come mossa di tempi morti, puoi usare una fiala di sangue per creare una Pozione di Salute Minore.'),
    'Minor Stamina Potion Recipe.md': ('Ricetta: Pozione di Stamina Minore', 'Come mossa di tempi morti, puoi usare l\'osso di una creatura per creare una Pozione di Stamina Minore.'),
    'Mythic Dust Recipe.md': ('Ricetta: Polvere Mistica', 'Come mossa di tempi morti, puoi usare una manciata di polvere d\'oro fine per creare Polvere Mistica.'),
    'Paragons Chain.md': ('Catena del Paragone', 'Come mossa di tempi morti, puoi meditare su un ideale o principio che ti sta a cuore e concentrare la tua volontà in questa catena. Una volta per riposo lungo, puoi spendere una Speranza per tirare un d20 come tuo Dado di Speranza per tiri che si allineano direttamente con quel principio.'),
    'Phoenix Feather.md': ('Piuma di Fenice', 'Se hai almeno una Piuma di Fenice addosso quando perdi conoscenza, ottieni un bonus di +1 al tiro che effettui per determinare se ottieni una cicatrice.'),
    'Piercing Arrows.md': ('Frecce Perforanti', 'Tre volte per riposo, quando hai successo su un attacco con una di queste frecce, puoi aggiungere la tua Competenza al tiro di danno.'),
    'Piper Whistle.md': ('Fischietto del Pifferaio', 'Questo fischietto artigianale ha un suono caratteristico. Quando soffi in questo fischietto, il suo tono penetrante può essere udito entro un raggio di 1 miglio.'),
    'Portal Seed.md': ('Seme del Portale', 'Puoi piantare questo seme nel terreno per far crescere un portale in quel punto. Il portale è pronto all\'uso in 24 ore. Puoi usare questo portale per viaggiare in qualsiasi altro luogo in cui hai piantato un seme di portale. Un portale può essere distrutto infliggendogli qualsiasi quantità di danni Magici.'),
    'Premium Bedroll.md': ('Sacco a pelo Premium', 'Durante i tempi morti, elimini automaticamente uno Stress.'),
    'Ring of Resistance.md': ('Anello di Resistenza', 'Una volta per riposo lungo, puoi attivare questo anello dopo un attacco riuscito contro di te per dimezzare i danni.'),
    'Ring of Silence.md': ('Anello del Silenzio', 'Spendi una Speranza per attivare questo anello. I tuoi passi sono silenziosi fino al tuo prossimo riposo.'),
    'Ring of Unbreakable Resolve.md': ('Anello di Determinazione Incrollabile', 'Una volta per sessione, quando il GM spende una Paura, puoi spendere 4 Speranza per annullare gli effetti di quella Paura spesa.'),
    'Shard of Memory.md': ('Scheggia di Memoria', 'Una volta per riposo lungo, puoi spendere 2 Speranza per richiamare una carta di dominio dal tuo archivio invece di pagare il suo Costo di Richiamo.'),
    'Skeleton Key.md': ('Chiave Scheletrica', 'Quando usi questa chiave per aprire una porta chiusa a chiave, ottieni vantaggio sul Tiro di Finezza.'),
    'Speaking Orbs.md': ('Sfere Parlanti', 'Questo paio di sfere permette a qualsiasi creatura che le tiene di comunicare tra loro a qualsiasi distanza.'),
    'Stride Relic.md': ('Reliquia del Passo', 'Ottieni un bonus di +1 alla tua Agilità. Puoi trasportare una sola reliquia.'),
    'Suspended Rod.md': ('Asta Sospesa', 'Questa asta piatta è incisa con rune. Quando attivi l\'asta, viene immediatamente sospesa in posizione. Finché l\'asta non viene disattivata, non può muoversi, non obbedisce alle regole della gravità e rimane in posizione.'),
    'Valorstone.md': ('Pietra del Valore', 'Puoi fissare questa pietra a un\'armatura che non ha già una caratteristica. L\'armatura ottiene la seguente caratteristica. Resiliente: Prima di segnare il tuo ultimo Slot di Armatura, tira un d6. Con un risultato di 6, riduci la gravità di una soglia senza segnare uno Slot di Armatura.'),
    'Vial of Darksmoke Recipe.md': ('Ricetta: Fiala di Fumo Oscuro', 'Come mossa di tempi morti, puoi segnare uno Stress per creare una Fiala di Fumo Oscuro.'),
    'Woven Net.md': ('Rete Intrecciata', 'Puoi effettuare un Tiro di Finezza usando questa rete per intrappolare una piccola creatura. Un bersaglio intrappolato può liberarsi con un Tiro di Attacco riuscito (16).'),
}

# ============================================================
# Translations for DaggerHeart Hope and Fear folder
# filename -> (translated_title, translated_description)
# ============================================================
hope_fear_translations = {
    'Augurs_Relic.md': ('Reliquia dell\'Augure', 'Una volta per riposo lungo, puoi attivare la tua caratteristica Speranza senza spendere Speranza. Puoi trasportare una sola reliquia.'),
    'Ball_Bearings.md': ('Sfere Metalliche', 'Questa borsa contiene sfere di metallo perfettamente lisce.'),
    'Blackwing_Quill.md': ('Piuma d\'Ala Nera', 'Questa penna d\'oca non finisce mai l\'inchiostro e non ha bisogno di essere affilata.'),
    'Boots_of_Supple_Mystique.md': ('Stivali della Mistica Sottile', 'Mentre indossi questi stivali, non lasci tracce o impronte.'),
    'Box_of_Dragon_Dust.md': ('Scatola di Polvere di Drago', 'Questa tabacchiera è piena di polvere combustibile.'),
    'Caltrops.md': ('Triboli', 'Puoi spargere questi triboli in un\'area Molto Vicina attorno a te. Una creatura che si affretta attraverso quell\'area deve segnare uno Stress.'),
    'Cheaters_Coin.md': ('Moneta del Baro', 'Quando lanci questa moneta, puoi spendere una Speranza per determinare su quale lato atterrerà.'),
    'Collapsible_Pole.md': ('Asta Pieghevole', 'Puoi smontare questa asta di 18 piedi in sei segmenti collegati di 3 piedi.'),
    'Collar_of_Ascendancy.md': ('Collare dell\'Ascendenza', 'Un animale che indossa questo collare ottiene la capacità di parlare e comprendere il linguaggio comune.'),
    'Communion_Relic.md': ('Reliquia della Comunione', 'Una volta per riposo, puoi spendere una Speranza per usare l\'Esperienza di un alleato come se fosse la tua. Puoi trasportare una sola reliquia.'),
    'Crucible_Frames.md': ('Occhiali del Crogiuolo', 'Questi occhiali rivelano i punti deboli di oggetti e creature. Tre volte per riposo, puoi spendere una Speranza per ottenere vantaggio su un tiro di attacco.'),
    'Dagginaes_Obsidian_Slate.md': ('Ardesia di Ossidiana di Dagginae', 'Questo foglio sottilissimo di vetro vulcanico è usato dagli archivisti per tenere appunti. Qualsiasi informazione incisa sulla sua superficie scompare ma può essere richiamata tramite un comando che imposti.'),
    'Eclipse_Coin.md': ('Moneta dell\'Eclissi', 'Una volta per riposo, lancia una moneta. Con testa, ottieni un bonus di +1 ai tiri di attacco fino al tuo prossimo attacco riuscito. Con croce, ottieni +1 alla tua Elusione finché un attacco non fallisce contro di te.'),
    'Elven_Spyglass.md': ('Cannocchiale Elfico', 'Puoi usare questo cannocchiale per ingrandire la tua vista di cento volte.'),
    'Enchanters_Loupe.md': ('Lente dell\'Incantatore', 'Puoi usare questa lente per vedere attraverso illusioni e incantesimi.'),
    'Eschers_Mirrorball.md': ('Sfera Specchiante di Escher', 'Una volta per riposo lungo, puoi comandare a questa sfera d\'argento delle dimensioni di un pugno di catturare un\'immagine omnidirezionale dei suoi dintorni sulla sua superficie. Questa immagine dura fino al tuo prossimo riposo lungo.'),
    'Force_Disc.md': ('Disco di Forza', 'Questo disco bidimensionale scintillante di forza magica ha un diametro di 4 piedi ed è magicamente legato a un sassolino. Il disco fluttua sempre 3 piedi a nord del sassolino e alla stessa elevazione. Il sassolino ha una massa pari a un centesimo della massa totale trasportata dal disco.'),
    'Furball_Bag.md': ('Borsa di Palle di Pelo', 'Una volta per riposo, puoi produrre da questa borsa 2d20 creature di pelo innocue, delle dimensioni di un gatto, di origine e specie indeterminate.'),
    'Gadimans_Backpack.md': ('Zaino di Gadiman', 'Una volta per riposo, puoi spendere una Speranza per evocare un oggetto comune fino a un piede cubico di dimensioni dentro questa sacca.'),
    'Ghoulskin_Gloves.md': ('Guanti di Pelle di Ghoul', 'Quando attacchi con un\'arma fisica mentre indossi questi guanti, i danni sono considerati sia fisici che magici.'),
    'Gloves_of_Alacrity.md': ('Guanti di Rapidità', 'Quando dovresti segnare uno Stress per ricaricare un\'arma, non lo segni.'),
    'Gourmet_Granules.md': ('Granuli Gourmet', 'Questa polvere saporita rende qualsiasi cibo su cui viene spruzzata delizioso e sano, non importa quanto sia insipido o marcio.'),
    'Grapnel.md': ('Rampino', 'Ottieni vantaggio sui tiri di azione per scalare superfici a strapiombo.'),
    'Gravewardens_Bell.md': ('Campana del Custode delle Tombe', 'Questa campana suona quando un fantasma o una creatura non morta si muove entro gittata Lontana da essa.'),
    'Heros_Helm.md': ('Elmo dell\'Eroe', 'Quando ottieni un successo critico su un attacco, tutti gli alleati entro gittata Vicina guadagnano una Speranza.'),
    'Hollowbark_Horn.md': ('Corno di Corteccia Cava', 'Puoi soffiare in questo corno per evocare una piccola creatura del bosco che esegua un compito semplice.'),
    'Insomniacs_Periapt.md': ('Periamma dell\'Insonne', 'Quando effettui un riposo senza recuperare Punti Ferita o Stress, ottieni un bonus di +2 ai tiri di attacco e danno fino al tuo prossimo riposo.'),
    'Iron_Dagger_Pendant.md': ('Ciondolo del Pugnale di Ferro', 'Una volta per riposo lungo, puoi spendere una Speranza per sussurrare al ciondolo il nome di una creatura. Il ciondolo ti tira dolcemente verso la posizione attuale di quella creatura fino al tuo prossimo riposo lungo.'),
    'Iron_Veil.md': ('Velo di Ferro', 'Questo copricapo a maglie di catena rende chi lo indossa invisibile alle creature fatate.'),
    'Kingfishers_Net.md': ('Rete del Martin Pescatore', 'Una volta per riposo lungo, puoi usare questa rete per pescare un pesce vivo da qualsiasi quantità d\'acqua, non importa quanto sia improbabile che quell\'acqua contenga pesci.'),
    'Knockback_Bracelets.md': ('Bracciali del Contraccolpo', 'Con un attacco con arma riuscito, puoi respingere il tuo bersaglio fino a gittata Vicina dalla sua posizione.'),
    'Loaded_Dice.md': ('Dadi Truccati', 'Puoi scegliere quale risultato tira questo set di dadi truccati con un Tiro di Finezza riuscito (14). Se tiri con Paura, chiunque guardi sa che i dadi sono truccati.'),
    'Mandragorian_Torch.md': ('Torcia Mandragorica', 'Questa torcia emette luce che solo chi la porta può vedere.'),
    'Map_of_Revelation.md': ('Mappa della Rivelazione', 'Puoi sintonizzare questa mappa su una creatura alla volta. La mappa mostra sempre la posizione della creatura sintonizzata.'),
    'Molepaw_Mittens.md': ('Guanti di Zampa di Talpa', 'Spendi una Speranza per nuotare attraverso la terra come se fosse acqua per i prossimi 10 minuti.'),
    'Namers_Oracle.md': ('Oracolo del Nominatore', 'Una volta per sessione, puoi tirare questo set di dadi runici per rivelare il nome completo dell\'ultima persona che hai toccato.'),
    'Nighthawkers_Ring.md': ('Anello del Falco Notturno', 'Spendi una Speranza per attivare la gemma in questo anello fino alla fine della scena. Mentre è attiva, la gemma cambia colore per indicare la vicinanza di chi la indossa a un tesoro nascosto: colori caldi per vicino, colori freddi per lontano.'),
    'Phobophages_Circlet.md': ('Cerchietto del Fobofago', 'Quando il GM spende una Paura, tira un d4. Una volta per scena, con un risultato di 4, elimini uno Stress.'),
    'Portal_Frames.md': ('Cornici del Portale', 'Questo paio di piccole cornici ornate, una rossa e una blu, sono collegate. Qualunque cosa passi in una esce dall\'altra.'),
    'Quillshawl.md': ('Scialle di Penne', 'Se un avversario ti attacca entro gittata di Mischia, deve avere successo su un Tiro di Reazione (12) o segnare un Punto Ferita.'),
    'Reliquary_of_the_Sightless_Saint.md': ('Reliquiario del Santo Cieco', 'Ottieni un bonus di +1 al tuo Dado di Speranza quando effettui la mossa di morte Rischia Tutto.'),
    'Returning_Ring.md': ('Anello del Ritorno', 'Quando lanci la tua arma principale mentre indossi questo anello, l\'arma riappare nella tua mano subito dopo l\'attacco.'),
    'Rings_of_Alliance.md': ('Anelli dell\'Alleanza', 'Due creature possono indossare questo paio di anelli d\'oro rosa. Una volta per sessione, puoi iniziare un Tiro di Squadra con chiunque indossi l\'altro anello senza spendere Speranza o contare contro il tuo limite di sessione per i Tiri di Squadra.'),
    'Rings_of_Camaraderie.md': ('Anelli della Camaraderie', 'Due creature possono indossare questo paio di anelli di legno. Puoi segnare lo Stress di chiunque indossi l\'altro anello (con il suo permesso) come se fosse il tuo.'),
    'Rings_of_Friendship.md': ('Anelli dell\'Amicizia', 'Due creature possono indossare questo paio di anelli a forma di serpenti avvolti. Puoi spendere la Speranza di chiunque indossi l\'altro anello (con il suo permesso) come se fosse la tua.'),
    'Self-Tying_Rope.md': ('Corda Autoannodante', 'Puoi comandare a questa corda di legarsi o slegarsi da sola.'),
    'Silees_Folding_Knife.md': ('Coltellino Pieghevole di Silee', 'Questa lama da 3 pollici ha un filo che taglia facilmente qualsiasi cosa tranne il manico in cui è conservata.'),
    'Sorcerers_Hat.md': ('Cappello dello Stregone', 'Questo cappello conico blu è coperto di stelle d\'argento. Una volta per riposo, puoi lanciare un incantesimo dal tuo archivio con un Costo di Richiamo pari o inferiore al tuo grado. Questo non funziona per le carte archiviate permanentemente.'),
    'Soul-Twin_Circlets.md': ('Cerchietti dell\'Anima Gemella', 'Due creature possono indossare questo paio di cerchietti. Puoi spendere una Speranza per scambiarti di posto con chiunque indossi l\'altro cerchietto.'),
    'Temporal_Sanctuary.md': ('Santuario Temporale', 'Un PG che effettua un riposo nel santuario temporale può scegliere una mossa di tempi morti aggiuntiva.'),
    'Thiefs_Compass.md': ('Bussola del Ladro', 'Questa bussola indica la via verso l\'uscita più vicina quando sei al chiuso e l\'ingresso più vicino quando sei all\'aperto.'),
    'Timekeepers_Pendant.md': ('Ciondolo del Cronometrista', 'Puoi scegliere una mossa di tempi morti aggiuntiva a ogni riposo.'),
    'Titans_Girdle.md': ('Cintura del Titano', 'Una volta per scena, puoi attivare questa cintura per ottenere un bonus di +1 alla tua Competenza per il tuo prossimo attacco.'),
    'Travelers_Bell.md': ('Campana del Viaggiatore', 'Una volta per riposo lungo, puoi suonare questa campana per aprire magicamente il percorso sicuro più breve attraverso un terreno accidentato per 1 ora.'),
    'Two-Faced_Aegis_Brooch.md': ('Spilla Egida dai Due Volti', 'Una volta per riposo, lancia una moneta. Con testa, diventi immune al prossimo danno fisico che subisci. Con croce, diventi immune al prossimo danno magico che subisci.'),
    'Warp_Pendant.md': ('Ciondolo del Varco', 'Una volta per riposo, segna uno Stress per teletrasportarti in un luogo che puoi vedere chiaramente.'),
    'Whisperstep_Anklet.md': ('Cavigliera del Passo Sussurrante', 'Questa cavigliera rende silenziosi i tuoi passi finché non ti muovi più veloce della velocità di camminata.'),
    'Wildriders_Saddle.md': ('Sella del Cavaliere Selvaggio', 'Questa sella concede a qualsiasi animale su cui è fissata la capacità di comprendere i comandi del suo cavaliere.'),
    'Windup_Toy.md': ('Giocattolo a Molla', 'Questo piccolo dispositivo meccanico ha la forma di un cucciolo di strixlupo e può essere programmato per eseguire semplici trucchi.'),
    'Zephyrs_Jar.md': ('Barattolo dello Zefiro', 'Puoi aprire questo barattolo vuoto durante un maltempo per catturare la tempesta e lasciare cieli sereni. La tempesta rimane dentro finché non viene scatenata riaprendo il barattolo.'),
}


def translate_file(filepath, title, description):
    """Translate a file by replacing title and description while preserving frontmatter."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the frontmatter block
    frontmatter_match = re.match(r'^(---\n.*?\n---\n)', content, re.DOTALL)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        body = content[frontmatter_match.end():]
    else:
        frontmatter = ''
        body = content

    # Replace title line (first # heading)
    body = re.sub(r'^# .*$', f'# {title}', body, count=1, flags=re.MULTILINE)

    lines = body.split('\n')
    new_lines = []
    i = 0
    while i < len(lines):
        # Format 1: has **_Item_** marker before description
        if lines[i].strip() == '**_Item_**':
            new_lines.append(lines[i])
            i += 1
            # Skip empty lines
            while i < len(lines) and lines[i].strip() == '':
                new_lines.append(lines[i])
                i += 1
            # Replace the description paragraph
            new_lines.append(description)
            i += 1
            # Skip the old description lines
            while i < len(lines) and lines[i].strip() != '':
                i += 1
        # Format 2: description is the first non-empty paragraph after the title
        elif re.match(r'^# ', lines[i].strip()):
            new_lines.append(lines[i])
            i += 1
            # Skip empty lines after title
            while i < len(lines) and lines[i].strip() == '':
                new_lines.append(lines[i])
                i += 1
            # Check if there's a **_Item_** marker after the title
            if lines[i].strip() == '**_Item_**':
                new_lines.append(lines[i])
                i += 1
                # Skip empty lines
                while i < len(lines) and lines[i].strip() == '':
                    new_lines.append(lines[i])
                    i += 1
            # Replace the description paragraph
            new_lines.append(description)
            i += 1
            # Skip the old description lines
            while i < len(lines) and lines[i].strip() != '':
                i += 1
        else:
            new_lines.append(lines[i])
            i += 1

    body = '\n'.join(new_lines)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + body)

    print(f'Translated: {filepath}')


# Process DaggerHeart folder
folder = '02_Meccaniche_DaggerHeart/Items/DaggerHeart'
for filename, (title, desc) in daggerheart_translations.items():
    filepath = os.path.join(folder, filename)
    if os.path.exists(filepath):
        translate_file(filepath, title, desc)
    else:
        print(f'NOT FOUND: {filepath}')

# Process DaggerHeart Hope and Fear folder
folder2 = '02_Meccaniche_DaggerHeart/Items/DaggerHeart Hope and Fear'
for filename, (title, desc) in hope_fear_translations.items():
    filepath = os.path.join(folder2, filename)
    if os.path.exists(filepath):
        translate_file(filepath, title, desc)
    else:
        print(f'NOT FOUND: {filepath}')

print('\nDone!')
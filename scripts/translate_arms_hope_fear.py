import os
import re

# ============================================================
# Translations for DaggerHeart Hope and Fear (Armi) folder
# filename -> (translated_title, translated_description)
# ============================================================
arms_hope_fear_translations = {
    'Adders_Fang.md': ("Dente di Vipera", "**_Velenoso: Quando infliggi danni Magici o superiori con questa arma, il bersaglio diventa temporaneamente Vulnerabile_**"),
    'Advanced_Arcane_Rifle.md': ("Fucile Arcano Avanzato", "**_Mira: Il tuo attacco ha svantaggio se il bersaglio è entro gittata Molto Vicina da te_**"),
    'Advanced_Brightsword.md': ("Brightsword Avanzata", ""),
    'Advanced_Casting_Dagger.md': ("Pugnale di Lancio Avanzato", "**_Versatile: Questa arma può anche essere usata con queste statistiche—Istinto, Mischia, d8+6_**"),
    'Advanced_Demon_Claw.md': ("Zanna del Demone Avanzata", "**_Incendiario: −1 a Agilità; con un attacco riuscito, tutte le creature entro gittata Molto Vicina del bersaglio devono segnare un Punto Ferita_**"),
    'Advanced_Enchanted_Chakram.md': ("Chakram Incantato Avanzato", "**_Rimbalzo: Quando lanci questa arma, torna nella tua mano_**"),
    'Advanced_Pickaxe.md': ("Piccozza Avanzata", "**_Scavo: Puoi usare questa arma per scavare nella terra e nella pietra a metà velocità normale_**"),
    'Advanced_Rocket_Maul.md': ("Mazza a Razzo Avanzata", "**_Concussivo: Con un attacco riuscito, puoi spendere una Speranza per respingere il bersaglio fino a gittata Lontana_**"),
    'Advanced_Rod.md': ("Asta Avanzata", "**_Conduttivo: Con un attacco riuscito, puoi spendere una Speranza per far scattare una scarica di fulmini verso un altro bersaglio_**"),
    'Advanced_Runelock_Pistol.md': ("Pistola a Rune Avanzata", "**_Ricarica: Dopo un attacco, tira un d6. Con un risultato di 1, devi segnare uno Stress per ricaricare_**"),
    'Advanced_Shadowblade.md': ("Lama dell'Ombra Avanzata", "**_Ultraterreno: Con un attacco riuscito, puoi infliggere danni fisici o magici_**"),
    'Amethyst_Glaive.md': ("Glaive di Ametista", "**_Spazzata: Con un attacco riuscito, puoi colpire una creatura aggiuntiva entro gittata di Mischia_**"),
    'Ancient_Spine_Whip.md': ("Frusta della Colonna Antica", "**_Intrappolante: Con un attacco riuscito, puoi spendere una Speranza per rendere il bersaglio temporaneamente Vulnerabile_**"),
    'Arc_Wand.md': ("Bastone dell'Arco", "**_Rimbalzo: Segna qualsiasi numero di Stress per colpire altrettante creature aggiuntive in gittata_**"),
    'Bastard_Sword.md': ("Spada Bastarda", "**_Pesante: Con un successo critico, il bersaglio segna anche uno Stress_**"),
    'Battlehammer.md': ("Martello da Guerra", "**_Frantumante: Con un successo critico, il bersaglio lascia cadere la sua arma equipaggiata_**"),
    'Beast_Bone_Blade.md': ("Lama d'Ossa di Bestia", "**_Primitivo: Quando sconfiggi una creatura con questa arma, ottieni Punti Ferita temporanei pari al tuo grado_**"),
    'Blade_of_Intent.md': ("Lama dell'Intenzione", "**_Ultraterreno: Con un attacco riuscito, puoi infliggere danni fisici o magici_**"),
    'Bone_Dagger.md': ("Pugnale d'Ossa", "**_Etereo: Puoi far apparire e scomparire questa arma a piacere. Scompare quando completi un Riposo_**"),
    'Bonebreaker_Maul.md': ("Mazza Frantumossa", "**_Distruttivo: −1 a Forza; con un attacco riuscito, tutti gli avversari entro gittata Molto Vicina devono segnare uno Stress_**"),
    'Brass_Knuckles.md': ("Nocche di Ottone", "**_Paio: +2 ai danni dell'arma primaria contro bersagli entro gittata di Mischia_**"),
    'Brightstone_Shieldblade.md': ("Lama-Scudo di Brightstone", "**_Protettivo: +2 al Punteggio di Armatura. Con un attacco riuscito, puoi trasferire la tua CA a un alleato entro gittata di Mischia_**"),
    'Casters_Wand.md': ("Bastone del Lanciatore", "**_Perforante: I danni inflitti con questa arma trattano la soglia Maggior del bersaglio come se avesse una penalità di −2_**"),
    'Chakram.md': ("Chakram", "**_Rimbalzo: Quando lanci questa arma, torna nella tua mano_**"),
    'Clockwork_Axe.md': ("Ascia a Molla", "**_Rapido: Quando effettui un attacco, puoi segnare uno Stress per colpire un'altra creatura in gittata_**"),
    'Club.md': ("Mazza", "**_Non letale: Quando un bersaglio segnerebbe qualsiasi numero di Punti Ferita da un attacco con questa arma, segna invece un numero uguale di Stress_**"),
    'Collapsible_Baton.md': ("Bastone Pieghevole", "**_Non letale: Quando un bersaglio segnerebbe qualsiasi numero di Punti Ferita da un attacco con questa arma, segna invece un numero uguale di Stress_**"),
    'Cruxite_Battle_Axe.md': ("Ascia da Guerra di Cruxite", "**_Distruttivo: −1 a Forza; con un attacco riuscito, l'equipaggiamento del bersaglio subisce una penalità di −1_**"),
    'Crystal_Crossbow.md': ("Arco da Caccia di Cristallo", "**_Rimbalzo: Segna qualsiasi numero di Stress per colpire altrettante creature aggiuntive in gittata dell'attacco_**"),
    'Crystal_Spear.md': ("Lancia di Cristallo", "**_Perforante: I danni inflitti con questa arma trattano la soglia Maggior del bersaglio come se avesse una penalità di −2_**"),
    'Dancing_Chain.md': ("Catena Danzante", "**_Estendibile: Puoi aumentare la gittata di questa arma fino a Molto Lontana. Ottieni una penalità di −1 ai tiri di attacco per ogni passo che aumenti_**"),
    'Darkstone_Gauntlets.md': ("Guantoni di Darkstone", "**_Velenoso: Quando infliggi danni Magici o superiori con questa arma, il bersaglio diventa temporaneamente Vulnerabile_**"),
    'Demons_Edge.md': ("Lama del Demone", "**_Disturbante: Quando sconfiggi una creatura con questa arma, tutti gli avversari entro gittata Vicina devono segnare uno Stress_**"),
    'Demon_Claw.md': ("Zanna del Demone", "**_Incendiario: −1 a Agilità; con un attacco riuscito, tutte le creature entro gittata Molto Vicina del bersaglio devono segnare un Punto Ferita_**"),
    'Dragon_Fang.md': ("Zanna del Drago", "**_Infernale: Con un attacco riuscito, il bersaglio segna 1 PF e non può recuperare PF fino alla fine del suo prossimo turno_**"),
    'Echo_Blade.md': ("Lama dell'Eco", "**_Risonante: Con un fallimento, puoi udire sussurri che ti concedono vantaggio sul tuo prossimo tiro di Percezione_**"),
    'Eldritch_Shards.md': ("Schegge Eldritch", "**_Frammentato: Puoi dividere i danni tra più bersagli entro gittata Molto Vicina_**"),
    'Eldritch_Vambrace.md': ("Vambrace Eldritch", "**_Deviante: Quando vieni attaccato, puoi segnare uno Slot di Armatura per ottenere un bonus alla tua Elusione pari al tuo Punteggio di Armatura_**"),
    'Elven_Longbow.md': ("Arco Lungo Elfico", "**_Silenzioso: Puoi effettuare attacchi con questa arma senza allertare le creature entro gittata Vicina_**"),
    'Elven_Shortbow.md': ("Arco Corto Elfico", "**_Silenzioso: Puoi effettuare attacchi con questa arma senza allertare le creature entro gittata Vicina_**"),
    'Enchanted_Rod.md': ("Asta Incantata", "**_Foco Arcano: I tuoi attacchi di incantesimo infliggono +2 danni con questa arma_**"),
    'Ethereal_Chains.md': ("Catene Etere", "**_Vincolante: Con un attacco riuscito, puoi spendere una Speranza per rendere il bersaglio temporaneamente Vincolato_**"),
    'Ethereal_Zweihänder.md': ("Zweihänder Etereo", "**_Etereo: Devi segnare uno Stress per evocare questa arma. Dura fino alla fine della scena_**"),
    'Ether_Shimmerer.md': ("Luccichio dell'Etere", "**_Spostamento di Fase: Con un attacco riuscito, puoi spendere una Speranza per teletrasportarti fino a gittata Molto Vicina_**"),
    'Fighting_Cloak.md': ("Mantello da Combattimento", "**_Imbottito: +2 alle soglie di danno_**"),
    'Firebrand.md': ("Brandeburgo", "**_Fiammeggiante: Con un attacco riuscito, il bersaglio prende fuoco e segna 1 PF all'inizio di ogni turno_**"),
    'Focus_Runes.md': ("Rune di Foco", "**_Focalizzato: +1 ai danni dell'arma primaria contro bersagli entro gittata Molto Vicina_**"),
    'Frostpiercer_Gauntlets.md': ("Guantoni del Perforatore di Ghiaccio", "**_Congelante: Con un attacco riuscito, il bersaglio diventa temporaneamente Vincolato e subisce danni da freddo_**"),
    'Ghost_Dagger.md': ("Pugnale Fantasma", "**_Fase: Gli attacchi con questa arma ignorano i bonus di copertura_**"),
    'Giants_Scepter.md': ("Scettro del Gigante", "**_Schiacciante: Con un successo critico, il bersaglio viene atterrato e segna uno Stress_**"),
    'Glacial_Lance.md': ("Lancia Glaciale", "**_Congelante: Con un attacco riuscito, il bersaglio diventa temporaneamente Vincolato_**"),
    'Gravity_Arbalest.md': ("Arbalesta della Gravità", "**_Magnetico: Quando effettui un attacco con questa arma, puoi spendere una Speranza per costringere tutti gli avversari entro gittata Molto Vicina a effettuare un Tiro di Reazione_**"),
    'Greater_Battlestaff.md': ("Grande Bastone da Guerra", "**_Catalitico: Con un attacco riuscito, puoi segnare uno Stress per concedere a un alleato entro gittata Vicina un bonus di +2 al suo prossimo tiro_**"),
    'Greater_Crystal_Crossbow.md': ("Grande Arco da Caccia di Cristallo", "**_Rimbalzo: Segna qualsiasi numero di Stress per colpire altrettante creature aggiuntive in gittata_**"),
    'Gunblade.md': ("Fucilame", "**_Versatile: Questa arma può anche essere usata con queste statistiche—Agilità, Mischia, d8+6 fis_**"),
    'Gunlance.md': ("Fucilancia", "**_Concussivo: Con un attacco riuscito, puoi spendere una Speranza per respingere il bersaglio fino a gittata Lontana_**"),
    'Hatchet.md': ("Ascia", "**_Seguito: Con un attacco riuscito con la tua arma primaria entro gittata di Mischia, puoi segnare uno Stress per ottenere un bonus di +1 alla tua Competenza per questo attacco_**"),
    'Holy_Water_Sprayer.md': ("Spray di Acqua Santa", "**_Bruciante: I bersagli entro gittata Molto Vicina dell'impatto devono segnare uno Stress o prendere fuoco, segnando 2 PF_**"),
    'Improved_Bastard_Sword.md': ("Spada Bastarda Migliorata", "**_Pesante: Con un successo critico, il bersaglio segna anche uno Stress_**"),
    'Improved_Brass_Knuckles.md': ("Nocche di Ottone Migliorate", "**_Paio: +3 ai danni dell'arma primaria contro bersagli entro gittata di Mischia_**"),
    'Improved_Combat_Knife.md': ("Coltello da Combattimento Migliorato", "**_Seghettato: Quando tiri un 1 su un dado di danno, infligge il danno completo indipendentemente dalla difesa del bersaglio_**"),
    'Improved_Fighting_Cloak.md': ("Mantello da Combattimento Migliorato", "**_Imbottito: +3 alle soglie di danno_**"),
    'Improved_Focus_Runes.md': ("Rune di Foco Migliorate", "**_Focalizzato: +1 ai danni dell'arma primaria contro bersagli entro gittata Molto Vicina_**"),
    'Improved_Hatchet.md': ("Ascia Migliorata", "**_Seguito: Con un attacco riuscito con la tua arma primaria entro gittata di Mischia, puoi segnare uno Stress per ottenere un bonus di +1_**"),
    'Improved_Rune_Shield.md': ("Scudo a Rune Migliorato", "**_Protettivo: +2 al Punteggio di Armatura_**"),
    'Improved_Throwing_Knives.md': ("Coltelli Lanciabili Migliorati", "**_Riserva: Puoi lanciare questa arma entro gittata Vicina effettuando un tiro di attacco usando Finezza_**"),
    'Iron_Collar.md': ("Collare di Ferro", "**_Vincolante: Con un attacco riuscito, puoi spendere una Speranza per vincolare il bersaglio_**"),
    'Katar.md': ("Katar", "**_Perforante: I danni inflitti con questa arma trattano la soglia Maggior del bersaglio come se avesse una penalità di −2_**"),
    'Legendary_Arcane_Rifle.md': ("Fucile Arcano Leggendario", "**_Mira: Il tuo attacco ha svantaggio se il bersaglio è entro gittata Molto Vicina da te_**"),
    'Legendary_Arquebus.md': ("Arquebus Leggendario", "**_Ricarica: Dopo un attacco, tira un d6. Con un risultato di 1, devi segnare uno Stress per ricaricare questa arma_**"),
    'Legendary_Bec_de_Corbin.md': ("Bec de Corbin Leggendario", "**_Devastante: Prima di effettuare un tiro di attacco, puoi segnare uno Stress per usare un d20 come dado di danno_**"),
    'Legendary_Black_Powder_Serpentine.md': ("Serpentina a Polvere Nera Leggendario", "**_Incendiario: −1 a Agilità; con un attacco riuscito, tutte le creature entro gittata Molto Vicina del bersaglio devono segnare un Punto Ferita_**"),
    'Legendary_Brass_Knuckles.md': ("Nocche di Ottone Leggendario", ""),
    'Legendary_Brightsword.md': ("Brightsword Leggendario", ""),
    'Legendary_Casting_Dagger.md': ("Pugnale di Lancio Leggendario", "**_Versatile: Questa arma può anche essere usata con queste statistiche—Istinto, Mischia, d8+9_**"),
    'Legendary_Clockwork_Crossbow.md': ("Arco da Caccia a Molla Leggendario", "**_Rapido: Quando effettui un attacco, puoi segnare uno Stress per colpire un'altra creatura in gittata_**"),
    'Legendary_Enchanted_Chakram.md': ("Chakram Incantato Leggendario", "**_Rimbalzo: Quando lanci questa arma, torna nella tua mano_**"),
    'Legendary_Infinite_Staff.md': ("Bastone Infinito Leggendario", "**_Estendibile: Puoi aumentare la gittata di questa arma fino a Molto Lontana. Ottieni una penalità di −1 ai tiri di attacco per ogni passo_**"),
    'Legendary_Katana.md': ("Katana Leggendario", "**_Rapido: Quando effettui un attacco, puoi segnare uno Stress per colpire un'altra creatura in gittata_**"),
    'Legendary_Rope_Dart.md': ("Lancia a Corda Leggendario", ""),
    'Legendary_Runelock_Pistol.md': ("Pistola a Rune Leggendario", "**_Ricarica: Dopo un attacco, tira un d6. Con un risultato di 1, devi segnare uno Stress per ricaricare_**"),
    'Legendary_Scimitar.md': ("Scimitarra Leggendario", ""),
    'Legendary_Severed_Dragon_Claw.md': ("Zanna del Drago Tronca Leggendario", "**_Distruttivo: −1 a Agilità; con un attacco riuscito, tutti gli avversari entro gittata Molto Vicina devono segnare uno Stress_**"),
    'Legendary_Shadowblade.md': ("Lama dell'Ombra Leggendario", "**_Ultraterreno: Con un attacco riuscito, puoi infliggere danni fisici o magici_**"),
    'Legendary_Twisted_Dagger.md': ("Pugnale Torsato Leggendario", "**_Perforante: I danni inflitti con questa arma trattano la soglia Maggior del bersaglio come se avesse una penalità di −2_**"),
    'Legendary_Whipsword.md': ("Spada-Frusta Leggendario", "**_Versatile: Questa arma può anche essere usata con queste statistiche—Finezza, Mischia, d10+9_**"),
    'Lightning_Edge.md': ("Lama del Fulmine", "**_Conduttivo: Con un attacco riuscito, il fulmine si scarica su una creatura vicina entro gittata Molto Vicina_**"),
    'Luminite_Blade.md': ("Lama di Luminite", "**_Illuminante: Questa arma emette luce brillante entro gittata di Mischia e luce fioca per gittata Molto Vicina_**"),
    'Luminite_Greatsword.md': ("Grande Spada di Luminite", "**_Illuminante: Questa arma emette luce brillante entro gittata di Mischia e luce fioca per gittata Molto Vicina_**"),
    'Obsidian_Greatsword.md': ("Grande Spada di Ossidiana", "**_Affilata: Questa arma infligge +2 danni con successi critici_**"),
    'Pickaxe.md': ("Piccozza", "**_Scavo: Puoi usare questa arma per scavare nella terra e nella pietra a metà velocità normale_**"),
    'Pile_of_Roots.md': ("Mucchio di Radici", "**_Intrappolante: Con un attacco riuscito, puoi spendere una Speranza per rendere il bersaglio temporaneamente Vulnerabile_**"),
    'Pile_of_Roots_Mk_II.md': ("Mucchio di Radici Mk II", "**_Intrappolante: Con un attacco riuscito, puoi spendere una Speranza per rendere il bersaglio temporaneamente Vulnerabile_**"),
    'Poison_Spitter.md': ("Sputa-Veleno", "**_Velenoso: Con un attacco riuscito, il bersaglio diventa temporaneamente Avvelenato_**"),
    'Rapier_of_Thorns.md': ("Stocco di Spine", "**_Spinato: Quando fallisci un attacco, il bersaglio segna comunque metà della tua Competenza come Stress_**"),
    'Razor_Wire.md': ("Filo di Rasoi", "**_Intrappolante: Con un attacco riuscito con la tua arma primaria contro un bersaglio entro gittata Molto Vicina, puoi spendere una Speranza per rendere il bersaglio temporaneamente Vulnerabile_**"),
    'Reinforced_Pickaxe.md': ("Piccozza Rinforzata", "**_Scavo: Puoi usare questa arma per scavare nella terra e nella pietra a metà velocità normale_**"),
    'Rime_Scepter.md': ("Scettro della Brina", "**_Congelante: Quando un attacco con questa arma fa segnare a un bersaglio 2 o più PF, questi diventa temporaneamente Vincolato_**"),
    'Ringing_War_Drum.md': ("Tamburo di Guerra Risonante", "**_Ispirante: Gli alleati entro gittata Vicina ottengono +1 ai tiri di danno mentre tieni questa arma_**"),
    'Rod_of_Force.md': ("Asta della Forza", "**_Forzuto: Con un attacco riuscito, puoi spendere una Speranza per spingere il bersaglio indietro fino a gittata Molto Vicina_**"),
    'Rune_Shield.md': ("Scudo a Rune", "**_Protettivo: +1 al Punteggio di Armatura_**"),
    'Segmented_Staff.md': ("Bastone Segmentato", "**_Doppio Uso: +1 al Punteggio di Armatura; +1 ai danni dell'arma primaria entro gittata di Mischia_**"),
    'Shadowhunter.md': ("Cacciatore d'Ombra", "**_Camminatore delle Tenebre: Puoi muoverti attraverso oggetti solidi e creature come se fossero terreno difficile_**"),
    'Silvered_Combat_Knife.md': ("Coltello da Combattimento Argentato", "**_Infallibile: Quando effettui un attacco con questa arma, puoi spendere una Speranza per colpire automaticamente_**"),
    'Spirit_Callers_Flute.md': ("Flauto del Chiamaspiriti", "**_Evocante: Quando completi un Riposo con questa arma, puoi evocare un alleato spirituale per una scena_**"),
    'Staff_of_Augma.md': ("Bastone di Augma", "**_Catalitico: Con un attacco riuscito, puoi segnare uno Stress per concedere a un alleato entro gittata Vicina un bonus di +3 al suo prossimo tiro di attacco_**"),
    'Starmetal_Blade.md': ("Lama di Starmetal", "**_Seghettato: Quando tiri un 1 su un dado di danno, infligge 8 danni invece_**"),
    'Storm_Gods_Greataxe.md': ("Grande Ascia del Dio della Tempesta", "**_Rimbalzo: Segna qualsiasi numero di Stress per colpire altrettante creature aggiuntive in gittata_**"),
    'Throwing_Knives.md': ("Coltelli Lanciabili", "**_Riserva: Puoi lanciare questa arma entro gittata Vicina effettuando un tiro di attacco usando Finezza_**"),
    'Tinkers_Hammer.md': ("Martello del Fabbro", "**_Versatile: Questa arma può anche essere usata con queste statistiche—Conoscenza, Mischia, d6+2_**"),
    'Venomfang_Rapier.md': ("Stocco Velenoso", "**_Velenoso: Quando infliggi danni Magici o superiori con questa arma, il bersaglio diventa temporaneamente Avvelenato_**"),
    'Void_Needle.md': ("Ago del Vuoto", "**_Etereo: Puoi far apparire e scomparire questa arma a piacere_**"),
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

    # Replace the title line (### heading)
    body = re.sub(r'^### .*$', f'### {title}', body, count=1, flags=re.MULTILINE)

    # Replace the description line (the **_..._** line)
    if description:
        # Replace the first **_..._** block
        body = re.sub(r'\*\*_[^*]*_\*\*', description, body, count=1)
    else:
        # Remove the description line if empty
        body = re.sub(r'\n\*\*_[^*]*_\*\*', '', body, count=1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + body)

    print(f'Translated: {filepath}')


def rename_file(filepath, new_name):
    """Rename a file replacing underscores with spaces."""
    directory = os.path.dirname(filepath)
    new_path = os.path.join(directory, new_name)
    if os.path.exists(new_path):
        print(f'WARNING: {new_path} already exists, skipping rename')
        return
    os.rename(filepath, new_path)
    print(f'Renamed: {filepath} -> {new_path}')


# Process the folder
folder = '02_Meccaniche_DaggerHeart/Armi/DaggerHeart Hope and Fear'
for filename, (title, desc) in arms_hope_fear_translations.items():
    filepath = os.path.join(folder, filename)
    if os.path.exists(filepath):
        translate_file(filepath, title, desc)
        # Rename: replace underscores with spaces
        new_name = filename.replace('_', ' ')
        rename_file(filepath, new_name)
    else:
        print(f'NOT FOUND: {filepath}')

print('\nDone!')

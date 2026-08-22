import os
import re

# Parole inglesi comuni per rilevamento
EN_WORDS = {
    'the', 'you', 'this', 'that', 'with', 'from', 'your', 'have', 'has', 'are',
    'can', 'when', 'gain', 'bonus', 'only', 'carry', 'one', 'relic', 'during',
    'downtime', 'automatically', 'clear', 'stress', 'these', 'two', 'point',
    'toward', 'other', 'matter', 'how', 'far', 'they', 'pair', 'allows', 'any',
    'creatures', 'holding', 'communicate', 'across', 'distance', 'locking',
    'cuffs', 'comes', 'key', 'while', 'inside', 'immune', 'damage', 'harmful',
    'effects', 'small', 'animal', 'companion', 'clay', 'behaves', 'example',
    'spider', 'can', 'weave', 'webs', 'bird', 'fly', 'retains', 'memory',
    'identity', 'across', 'forms', 'but', 'take', 'new', 'ways', 'each', 'form',
    'shape', 'ball', 'into', 'when', 'you', 'successful', 'attack', 'arrow',
    'stored', 'quiver', 'gain', 'damage', 'roll', 'equal', 'your', 'current',
    'tier', 'when', 'about', 'mark', 'your', 'last', 'roll', 'result', 'higher',
    'don', 't', 'open', 'small', 'box', 'once', 'per', 'long', 'rest', 'd12',
    'empty', 'contains', 'common', 'consumable', 'random', 'two', 'common',
    'consumables', 'random', 'gain', 'bonus', 'your', 'strength', 'can',
    'carry', 'only', 'one', 'relic', 'gain', 'bonus', 'your', 'presence',
    'can', 'carry', 'only', 'one', 'relic', 'explosive', 'rounds', 'when',
    'use', 'these', 'ammunition', 'hit', 'deals', 'extra', 'damage', 'each',
    'creature', 'adjacent', 'target', 'climbing', 'speed', 'equal', 'your',
    'movement', 'speed', 'instinct', 'finesse', 'mind', 'soul', 'body',
    'perception', 'intelligence', 'wisdom', 'charisma', 'dexterity',
    'constitution', 'strength', 'spirit', 'magic', 'spell', 'cast', 'casting',
    'roll', 'bonus', 'target', 'ally', 'allies', 'within', 'near', 'range',
    'active', 'cannot', 'moved', 'deactivated', 'reactivated', 'next', 'long',
    'rest', 'torch', 'magical', 'will', 'flame', 'light', 'fills', 'space',
    'much', 'larger', 'should', 'enough', 'illuminate', 'cavern', 'bright',
    'day', 'cloak', 'creature', 'spell', 'trait', 'wearing', 'adjust', 'color',
    'texture', 'size', 'will', 'amulet', 'attach', 'weapon', 'melee', 'range',
    'trait', 'three', 'times', 'per', 'rest', 'activate', 'make', 'near',
    'range', 'attack', 'instead', 'melee', 'gloves', 'wear', 'climbing',
    'speed', 'equal', 'movement', 'speed', 'glider', 'fall', 'slow', 'descent',
    'land', 'safely', 'feather', 'phoenix', 'revive', 'death', 'once', 'per',
    'rest', 'return', 'life', 'full', 'health', 'stone', 'gem', 'precision',
    'mighty', 'insight', 'audacity', 'sagacity', 'alacrity', 'valor', 'great',
    'blood', 'dark', 'smoke', 'mythic', 'dust', 'health', 'potion', 'stamina',
    'potion', 'recipe', 'minor', 'major', 'ring', 'resistance', 'silence',
    'unbreakable', 'resolve', 'chain', 'paragon', 'skeleton', 'key', 'lock',
    'pick', 'memory', 'shard', 'portal', 'seed', 'whistle', 'piper', 'arrows',
    'piercing', 'net', 'woven', 'flask', 'dual', 'elusive', 'amulet', 'empty',
    'chest', 'fire', 'jar', 'flickerfly', 'pendant', 'hopekeeper', 'locket',
    'infinite', 'bag', 'lakestrider', 'boots', 'lorekeeper', 'corrector',
    'sprite', 'belt', 'unity', 'ficklesand', 'bag', 'greatstone', 'valorstone',
    'bloodstone', 'glamour', 'stone', 'glider', 'suspended', 'rod', 'woven',
    'net', 'piercing', 'arrows', 'piper', 'whistle', 'portal', 'seed', 'shard',
    'memory', 'skeleton', 'key', 'ring', 'resistance', 'ring', 'silence',
    'ring', 'unbreakable', 'resolve', 'paragons', 'chain', 'phoenix', 'feather',
    'minor', 'health', 'potion', 'recipe', 'minor', 'stamina', 'potion',
    'recipe', 'mythic', 'dust', 'recipe', 'vial', 'darksmoke', 'recipe',
    'fire', 'jar', 'flickerfly', 'pendant', 'hopekeeper', 'locket', 'infinite',
    'bag', 'lakestrider', 'boots', 'lorekeeper', 'corrector', 'sprite',
    'belt', 'unity', 'bag', 'ficklesand', 'greatstone', 'valorstone',
    'bloodstone', 'glamour', 'stone', 'glider', 'suspended', 'rod', 'woven',
    'net', 'piercing', 'arrows', 'piper', 'whistle', 'portal', 'seed', 'shard',
    'memory', 'skeleton', 'key', 'ring', 'resistance', 'ring', 'silence',
    'ring', 'unbreakable', 'resolve', 'paragons', 'chain', 'phoenix', 'feather',
    'minor', 'health', 'potion', 'recipe', 'minor', 'stamina', 'potion',
    'recipe', 'mythic', 'dust', 'recipe', 'vial', 'darksmoke', 'recipe'
}

def detect_language(content):
    """Rileva se il contenuto è in inglese basandosi su parole chiave"""
    text = content.lower()
    # Conta le parole inglesi comuni
    en_count = sum(1 for word in EN_WORDS if re.search(r'\b' + word + r'\b', text))
    return en_count

base = '02_Meccaniche_Daggerheart/Items'
for root, dirs, files in os.walk(base):
    for f in sorted(files):
        if not f.endswith('.md'):
            continue
        path = os.path.join(root, f)
        with open(path, 'r', encoding='utf-8') as fh:
            content = fh.read()
        # Estrai il corpo del testo (dopo il frontmatter)
        body = content.split('---', 2)[-1] if content.startswith('---') else content
        score = detect_language(body)
        status = 'EN' if score >= 3 else 'IT'
        print(f'{status} | {path} | score={score}')
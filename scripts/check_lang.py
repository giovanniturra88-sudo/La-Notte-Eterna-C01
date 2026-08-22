import os
import re

def check_file_lang(filepath):
    """Check if a file is in English by looking for English keywords."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # English keywords to look for
    english_keywords = [
        r'\b(the|you|and|with|your|this|that|gain|advantage|spend|hope|fear|roll|attack|target|creature|item|weapon|armor|once|per|session|long|short|rest|can|may|when|while|if|then|also|instead|additional|damage|dice|die|check|success|fail|potion|scroll|potion)\b',
        r'\b(Common|Uncommon|Rare|Very Rare|Legendary|Artifact)\b',
        r'# [A-Z][a-z]+ [A-Z][a-z]+',
    ]
    
    score = 0
    for pattern in english_keywords:
        matches = re.findall(pattern, content, re.IGNORECASE)
        score += len(matches)
    
    # Italian keywords
    italian_keywords = [
        r'\b(il|lo|la|gli|le|un|uno|una|con|per|puoi|ottieni|vantaggio|spendere|speranza|paura|tiro|attacco|bersaglio|creatura|oggetto|arma|armatura|volta|sessione|riposo|lungo|corto|quando|mentre|se|allora|anche|invece|aggiuntivo|danno|dadi|dado|controllo|successo|fallimento|pozione|pergamena|comune|non comune|raro|molto raro|leggendario|manufatto)\b',
        r'# [A-ZÀ-Ž][a-zà-ž]+ [A-ZÀ-Ž][a-zà-ž]+',
    ]
    
    italian_score = 0
    for pattern in italian_keywords:
        matches = re.findall(pattern, content, re.IGNORECASE)
        italian_score += len(matches)
    
    # Determine language
    if score > italian_score:
        return 'EN'
    elif italian_score > score:
        return 'IT'
    else:
        return 'UNKNOWN'

# Check all files in both folders
folders = [
    '02_Meccaniche_DaggerHeart/Items/DaggerHeart',
    '02_Meccaniche_DaggerHeart/Items/DaggerHeart Hope and Fear'
]
for folder in folders:
    print(f'\n=== {folder} ===')
    for f in os.listdir(folder):
        if f.endswith('.md'):
            filepath = os.path.join(folder, f)
            lang = check_file_lang(filepath)
            print(f'{f}: {lang}')

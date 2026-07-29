import os
import re
import json
from collections import defaultdict

def extract_aliases_from_file(filepath):
    """Extract aliases from a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for the alias field in YAML frontmatter
        alias_match = re.search(r'alias:\s*(\[.*?\])', content, re.DOTALL)
        
        if alias_match:
            aliases_str = alias_match.group(1)
            # Extract individual aliases from the array
            aliases = re.findall(r'"([^"]*)"', aliases_str)
            return aliases
        return []
        
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return []

def generate_alias_dictionary(folder_path):
    """Generate a dictionary of all aliases with their occurrences"""
    alias_info = {}
    
    # Process all .md files
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            filepath = os.path.join(folder_path, filename)
            aliases = extract_aliases_from_file(filepath)
            
            if aliases:
                # Store the original filename and its aliases
                alias_info[filename] = {
                    'aliases': aliases,
                    'count': len(aliases)
                }
    
    return alias_info

def main():
    """Main function to generate JSON dictionary of aliases"""
    folder_path = "../02_Meccaniche_DaggerHeart/Armi_Daggerheart"
    
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} not found")
        return
    
    print("Generazione dizionario dei sinonimi...")
    
    alias_dictionary = generate_alias_dictionary(folder_path)
    
    # Save to JSON file
    output_file = "alias_dictionary.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(alias_dictionary, f, ensure_ascii=False, indent=2)
    
    print(f"Dizionario dei sinonimi salvato in: {output_file}")
    
    # Also create a simplified version for easy reference
    print("\n" + "=" * 50)
    print("Contenuto del dizionario:")
    print("=" * 50)
    
    # Create a flat list of all aliases with their files
    all_aliases = defaultdict(list)
    for filename, info in alias_dictionary.items():
        for alias in info['aliases']:
            all_aliases[alias].append(filename)
    
    print("Sinonimi unici e i file che li contengono:")
    for alias, files in sorted(all_aliases.items()):
        print(f"\n{alias}:")
        for file in sorted(files):
            print(f"  - {file}")
    
    # Summary statistics
    total_files = len(alias_dictionary)
    total_aliases = sum(len(info['aliases']) for info in alias_dictionary.values())
    unique_aliases = len(all_aliases)
    
    print(f"\n" + "=" * 50)
    print("STATISTICHE:")
    print("=" * 50)
    print(f"Numero totale di file con sinonimi: {total_files}")
    print(f"Numero totale di sinonimi: {total_aliases}")
    print(f"Numero di sinonimi unici: {unique_aliases}")

if __name__ == "__main__":
    main()
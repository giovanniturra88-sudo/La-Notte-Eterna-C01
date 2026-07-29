import os
import re
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

def list_all_aliases(folder_path):
    """List all aliases from all files in the folder"""
    all_aliases = defaultdict(list)
    
    # Process all .md files
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            filepath = os.path.join(folder_path, filename)
            aliases = extract_aliases_from_file(filepath)
            
            if aliases:
                # Store the original filename and its aliases
                all_aliases[filename] = aliases
    
    return all_aliases

def main():
    """Main function to list all aliases"""
    folder_path = "../02_Meccaniche_DaggerHeart/Armi_Daggerheart"
    
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} not found")
        return
    
    print("Elenco di tutti i sinonimi presenti nei file delle armi:")
    print("=" * 60)
    
    all_aliases = list_all_aliases(folder_path)
    
    # Sort files alphabetically
    sorted_files = sorted(all_aliases.keys())
    
    for filename in sorted_files:
        aliases = all_aliases[filename]
        print(f"\n{filename}:")
        for alias in aliases:
            print(f"  - {alias}")
    
    # Also create a summary of all unique aliases
    print("\n" + "=" * 60)
    print("SINONIMI UNICI:")
    print("=" * 60)
    
    all_unique_aliases = set()
    for filename in sorted_files:
        aliases = all_aliases[filename]
        for alias in aliases:
            all_unique_aliases.add(alias)
    
    # Sort and display unique aliases
    sorted_aliases = sorted(all_unique_aliases)
    for alias in sorted_aliases:
        print(f"  - {alias}")
    
    print(f"\nTotale file con alias: {len([f for f in sorted_files if all_aliases[f]])}")
    print(f"Totale sinonimi unici: {len(sorted_aliases)}")

if __name__ == "__main__":
    main()

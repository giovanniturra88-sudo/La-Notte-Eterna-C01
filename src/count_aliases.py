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

def count_aliases(folder_path):
    """Count occurrences of all aliases and track empty fields"""
    alias_count = defaultdict(int)
    total_files = 0
    files_with_aliases = 0
    files_without_aliases = 0
    
    # Process all .md files
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            filepath = os.path.join(folder_path, filename)
            aliases = extract_aliases_from_file(filepath)
            
            total_files += 1
            
            if aliases:
                files_with_aliases += 1
                for alias in aliases:
                    alias_count[alias] += 1
            else:
                files_without_aliases += 1
    
    return alias_count, total_files, files_with_aliases, files_without_aliases

def main():
    """Main function to count all aliases"""
    folder_path = "../02_Meccaniche_DaggerHeart/Armi_Daggerheart"
    
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} not found")
        return
    
    print("Analisi dei sinonimi nelle armi:")
    print("=" * 50)
    
    alias_count, total_files, files_with_aliases, files_without_aliases = count_aliases(folder_path)
    
    print(f"Numero totale di file: {total_files}")
    print(f"File con sinonimi: {files_with_aliases}")
    print(f"File senza sinonimi: {files_without_aliases}")
    print(f"Percentuale di file con sinonimi: {(files_with_aliases/total_files)*100:.1f}%")
    
    print("\n" + "=" * 50)
    print("CONTeggio dei sinonimi (ordinati per frequenza):")
    print("=" * 50)
    
    # Sort by count (descending)
    sorted_aliases = sorted(alias_count.items(), key=lambda x: x[1], reverse=True)
    
    for alias, count in sorted_aliases:
        print(f"{count:2d} volte: {alias}")
    
    print("\n" + "=" * 50)
    print("Sinonimi unici totali: ", len(alias_count))
    
    if alias_count:
        print("Sinonimo più frequente:", max(alias_count.items(), key=lambda x: x[1])[0])
        print("Numero di occorrenze del sinonimo più frequente:", max(alias_count.items(), key=lambda x: x[1])[1])

if __name__ == "__main__":
    main()
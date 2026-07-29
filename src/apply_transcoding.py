import os
import re
import json
from collections import defaultdict

def read_transcoding_table():
    """Read the transcoding table from JSON file"""
    try:
        with open('transcoding_table.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("File transcoding_table.json non trovato")
        return None

def extract_properties_from_file(filepath):
    """Extract all properties from a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract YAML frontmatter
        yaml_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL | re.MULTILINE)
        
        properties = {}
        if yaml_match:
            yaml_content = yaml_match.group(1)
            for line in yaml_content.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip()
                    properties[key] = value
        
        return properties, content
        
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return {}, ""

def update_file_properties(filepath, transcoding_table):
    """Update file properties using transcoding table"""
    try:
        # Read current file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract YAML frontmatter
        yaml_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL | re.MULTILINE)
        
        if not yaml_match:
            print(f"File {filepath} non contiene YAML frontmatter")
            return False
        
        yaml_content = yaml_match.group(1)
        new_yaml_content = []
        
        # Parse current properties
        current_properties = {}
        for line in yaml_content.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                current_properties[key] = value
        
        # Apply transcoding
        updated = False
        for prop, value in current_properties.items():
            if prop in transcoding_table['detailed_mapping']:
                mapping = transcoding_table['detailed_mapping'][prop]
                if value in mapping:
                    # Check if we need to change the value
                    new_value = mapping[value]
                    if new_value != value:
                        print(f"Aggiornamento {prop}: '{value}' -> '{new_value}'")
                        current_properties[prop] = new_value
                        updated = True
        
        # Rebuild YAML content
        lines = content.split('\n')
        yaml_start = 0
        yaml_end = 0
        
        # Find the YAML section boundaries
        for i, line in enumerate(lines):
            if line.strip() == '---':
                if yaml_start == 0:
                    yaml_start = i
                else:
                    yaml_end = i
                    break
        
        # Rebuild the YAML section with updated values
        new_yaml_lines = ['---']
        for prop, value in current_properties.items():
            new_yaml_lines.append(f"{prop}: {value}")
        new_yaml_lines.append('---')
        
        # Replace the old YAML section with the new one
        new_lines = lines[:yaml_start+1] + new_yaml_lines + lines[yaml_end:]
        
        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        
        if updated:
            print(f"File aggiornato: {os.path.basename(filepath)}")
        else:
            print(f"Nessun aggiornamento necessario: {os.path.basename(filepath)}")
            
        return True
        
    except Exception as e:
        print(f"Error updating {filepath}: {e}")
        return False

def main():
    """Main function to apply transcoding to all files"""
    folder_path = "../02_Meccaniche_DaggerHeart/Armi_Daggerheart"
    
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} not found")
        return
    
    # Read transcoding table
    transcoding_table = read_transcoding_table()
    if not transcoding_table:
        return
    
    print("Applicazione della transcodifica ai file...")
    print("=" * 50)
    
    # Process all .md files
    updated_files = 0
    total_files = 0
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            filepath = os.path.join(folder_path, filename)
            total_files += 1
            
            if update_file_properties(filepath, transcoding_table):
                updated_files += 1
    
    print("\n" + "=" * 50)
    print("RIEPILOGO:")
    print("=" * 50)
    print(f"File totali processati: {total_files}")
    print(f"File aggiornati: {updated_files}")

if __name__ == "__main__":
    main()
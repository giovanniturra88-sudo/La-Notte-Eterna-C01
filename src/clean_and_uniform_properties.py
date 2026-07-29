import os
import re
import json
from collections import defaultdict

def extract_properties_from_file(filepath):
    """Extract properties from a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract YAML frontmatter (first section)
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

def clean_and_uniform_file(filepath):
    """Clean and uniform file properties"""
    try:
        # Read current file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the first YAML section (we'll keep only this one)
        yaml_matches = re.findall(r'^---\n(.*?)\n---', content, re.DOTALL | re.MULTILINE)
        
        if len(yaml_matches) >= 1:
            # Keep only the first YAML section
            first_yaml = yaml_matches[0]
            
            # Parse properties from first YAML
            properties = {}
            for line in first_yaml.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip()
                    properties[key] = value
            
            # Uniform properties (lowercase, standardize values)
            uniformed_properties = {}
            
            for prop, value in properties.items():
                # Standardize property names
                if prop.lower() == 'type':
                    uniformed_properties['type'] = value.lower() if value else value
                elif prop.lower() == 'original_name':
                    uniformed_properties['original_name'] = value
                elif prop.lower() == 'alias':
                    uniformed_properties['alias'] = value  # Keep as is for now
                elif prop.lower() == 'categoria':
                    uniformed_properties['categoria'] = value.lower() if value else value
                elif prop.lower() == 'tier':
                    uniformed_properties['tier'] = value
                elif prop.lower() == 'ruolo':
                    uniformed_properties['ruolo'] = value.lower() if value else value
                elif prop.lower() == 'tipo_danno':
                    uniformed_properties['tipo_danno'] = value.lower() if value else value
                elif prop.lower() == 'tratto':
                    uniformed_properties['tratto'] = value.lower() if value else value
                elif prop.lower() == 'gittata':
                    uniformed_properties['gittata'] = value.lower() if value else value
                elif prop.lower() == 'danno':
                    uniformed_properties['danno'] = value
                elif prop.lower() == 'ingombro':
                    uniformed_properties['ingombro'] = value.lower() if value else value
                else:
                    uniformed_properties[prop] = value
            
            # Rebuild YAML section with uniformed properties
            new_yaml_lines = ['---']
            for prop, value in sorted(uniformed_properties.items()):
                new_yaml_lines.append(f"{prop}: {value}")
            new_yaml_lines.append('---')
            
            new_yaml_content = '\n'.join(new_yaml_lines)
            
            # Replace both YAML sections with the cleaned one
            lines = content.split('\n')
            new_lines = []
            
            yaml_found = False
            for line in lines:
                if line.strip() == '---' and not yaml_found:
                    # First ---, replace with our clean YAML
                    new_lines.append(new_yaml_content)
                    yaml_found = True
                elif line.strip() == '---' and yaml_found:
                    # Second ---, skip it
                    continue
                elif not yaml_found or not (line.strip() == '---'):
                    # Skip lines from second YAML section
                    if not yaml_found or not (line.strip() == '---'):
                        new_lines.append(line)
            
            # Write back to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write('\n'.join(new_lines))
            
            print(f"File aggiornato: {os.path.basename(filepath)}")
            return True
            
    except Exception as e:
        print(f"Error updating {filepath}: {e}")
        return False

def main():
    """Main function to clean and uniform all files"""
    folder_path = "../02_Meccaniche_DaggerHeart/Armi_Daggerheart"
    
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} not found")
        return
    
    print("Pulizia e uniformazione delle proprietà nei file...")
    print("=" * 60)
    
    # Process all .md files
    processed_files = 0
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            filepath = os.path.join(folder_path, filename)
            if clean_and_uniform_file(filepath):
                processed_files += 1
    
    print("\n" + "=" * 60)
    print("RIEPILOGO:")
    print("=" * 60)
    print(f"File processati: {processed_files}")

if __name__ == "__main__":
    main()
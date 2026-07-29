import os
import re
from collections import defaultdict

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
        
        return properties
        
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return {}

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

def list_aliases_by_property(folder_path):
    """List all aliases organized by property"""
    file_properties = {}
    
    # Process all .md files
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            filepath = os.path.join(folder_path, filename)
            properties = extract_properties_from_file(filepath)
            aliases = extract_aliases_from_file(filepath)
            
            if aliases:
                file_properties[filename] = {
                    'properties': properties,
                    'aliases': aliases
                }
    
    return file_properties

def main():
    """Main function to list all aliases organized by property"""
    folder_path = "../02_Meccaniche_DaggerHeart/Armi_Daggerheart"
    
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} not found")
        return
    
    print("Elenco di tutti i sinonimi presenti nei file delle armi, suddivisi per proprietà:")
    print("=" * 80)
    
    file_properties = list_aliases_by_property(folder_path)
    
    # Sort files alphabetically
    sorted_files = sorted(file_properties.keys())
    
    # Group by property values to show how they're distributed
    property_groups = defaultdict(lambda: defaultdict(list))
    
    for filename in sorted_files:
        props = file_properties[filename]['properties']
        aliases = file_properties[filename]['aliases']
        
        print(f"\n{filename}:")
        print("  Proprietà:")
        for prop, value in props.items():
            print(f"    {prop}: {value}")
        
        if aliases:
            print("  Sinonimi:")
            for alias in aliases:
                print(f"    - {alias}")
                
                # Group by different properties for better organization
                for prop, value in props.items():
                    if prop not in ['original_name', 'type', 'categoria']:
                        property_groups[prop][value].append((filename, alias))
    
    print("\n" + "=" * 80)
    print("SINONIMI GRUPPATI PER PROPRIETÀ:")
    print("=" * 80)
    
    for prop, values in property_groups.items():
        print(f"\n{prop}:")
        for value, items in values.items():
            print(f"  {value}: {len(items)}")
            """
            for filename, alias in items:
                print(f"    - {alias} ({filename})")
            """

if __name__ == "__main__":
    main()
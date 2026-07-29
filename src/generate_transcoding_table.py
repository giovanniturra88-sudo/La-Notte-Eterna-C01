import os
import re
import json
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

def generate_transcoding_table(folder_path):
    """Generate transcoding table for all properties"""
    property_values = defaultdict(lambda: defaultdict(int))  # property -> value -> count
    file_properties = {}
    
    # Process all .md files
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            filepath = os.path.join(folder_path, filename)
            properties = extract_properties_from_file(filepath)
            aliases = extract_aliases_from_file(filepath)
            
            file_properties[filename] = {
                'properties': properties,
                'aliases': aliases
            }
            
            # Count all property values
            for prop, value in properties.items():
                if prop != 'alias':  # Skip alias field itself
                    property_values[prop][value] += 1
    
    return property_values, file_properties

def main():
    """Main function to generate transcoding table"""
    folder_path = "../02_Meccaniche_DaggerHeart/Armi_Daggerheart"
    
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} not found")
        return
    
    print("Generazione tabella di transcodifica...")
    
    property_values, file_properties = generate_transcoding_table(folder_path)
    
    # Create transcoding table structure
    transcoding_table = {}
    
    print("\n" + "=" * 60)
    print("VALORI PER OGNI PROPRIETÀ:")
    print("=" * 60)
    
    for prop, values in property_values.items():
        print(f"\n{prop}:")
        sorted_values = sorted(values.items(), key=lambda x: x[1], reverse=True)
        
        # Store all unique values for this property
        transcoding_table[prop] = {
            'values': [value for value, count in sorted_values],
            'count': len(sorted_values)
        }
        
        for value, count in sorted_values:
            print(f"  {count:2d} volte: {value}")
    
    # Generate a more detailed transcoding table
    detailed_transcoding = {}
    
    print("\n" + "=" * 60)
    print("TABELLA DI TRANSCODIFICA DETTAGLIATA:")
    print("=" * 60)
    
    for prop, values in property_values.items():
        print(f"\n{prop}:")
        print("  Valori trovati:")
        
        # Create mapping from each value to a standardized form
        value_mapping = {}
        sorted_values = sorted(values.items(), key=lambda x: x[1], reverse=True)
        
        for i, (value, count) in enumerate(sorted_values):
            # Create a standardized key (you can customize this logic)
            standardized_key = value.replace(' ', '_').lower() if value else 'empty'
            value_mapping[value] = standardized_key
            print(f"    {count:2d} volte -> '{value}' -> '{standardized_key}'")
        
        detailed_transcoding[prop] = value_mapping
    
    # Save the transcoding table to JSON
    output_file = "transcoding_table.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'property_values': dict(property_values),
            'detailed_mapping': detailed_transcoding
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\nTabella di transcodifica salvata in: {output_file}")
    
    # Also create a simple mapping file for easy editing
    mapping_file = "alias_mapping.json"
    mapping_data = {}
    
    for prop, values in property_values.items():
        if prop == 'original_name':  # Skip original names
            continue
            
        mapping_data[prop] = {}
        sorted_values = sorted(values.items(), key=lambda x: x[1], reverse=True)
        
        print(f"\nProprietà '{prop}' - Suggerimenti per uniformità:")
        for i, (value, count) in enumerate(sorted_values):
            if i == 0:
                # First value is likely the standard
                mapping_data[prop]['standard'] = value
                print(f"  Standard: '{value}'")
            else:
                print(f"  Alternativa: '{value}'")
    
    with open(mapping_file, 'w', encoding='utf-8') as f:
        json.dump(mapping_data, f, ensure_ascii=False, indent=2)
    
    print(f"\nMappatura semplificata salvata in: {mapping_file}")
    
    # Summary
    print("\n" + "=" * 60)
    print("RIEPILOGO:")
    print("=" * 60)
    total_properties = len(property_values)
    print(f"Numero totale di proprietà analizzate: {total_properties}")
    
    total_unique_values = sum(len(values) for values in property_values.values())
    print(f"Numero totale di valori unici trovati: {total_unique_values}")

if __name__ == "__main__":
    main()
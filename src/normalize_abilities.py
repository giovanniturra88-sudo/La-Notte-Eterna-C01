import os
import re
import sys

import os
import re

def extract_values_from_markdown(content):
    """Extract values from markdown format - simplified approach"""
    lines = content.split('\n')
    values = {}
    
    # Look for the pattern in the first few lines
    for line in lines[:5]:  # Check first 5 lines only
        if '**_Livello' in line and '_**' in line:
            # Extract level
            level_match = re.search(r'\*\*_Livello (\d+)\*\*', line)
            if level_match:
                values['Livello'] = level_match.group(1)
                
        if 'Abilità [[' in line:
            # Extract domain
            domain_match = re.search(r'Abilità \[\[(.*?)\]\]', line)
            if domain_match:
                values['Dominio'] = f"[[{domain_match.group(1)}]]"
                
        if '**_Costo di Richiamo_' in line and '_**' in line:
            # Extract cost
            cost_match = re.search(r'\*\*_Costo di Richiamo\*\*.*?_(\d+)_', line)
            if cost_match:
                values['Costo di Richiamo'] = cost_match.group(1)
    
    return values

def create_yaml_frontmatter(values, filename):
    """Create YAML frontmatter with extracted values"""
    # Default values for missing fields
    if 'Livello' not in values:
        values['Livello'] = '1'
    if 'Dominio' not in values:
        values['Dominio'] = '[[Nessuno]]'
    if 'Costo di Richiamo' not in values:
        values['Costo di Richiamo'] = '0'
    
    # Set other required fields with sensible defaults or extract from filename
    values['Titolo Inglese'] = filename.replace('.md', '')
    values['Tipologia Carta'] = '[[Abilità]]'
    
    # Create YAML frontmatter
    lines = ['---']
    # Fields in consistent order
    field_order = ['Livello', 'Dominio', 'Costo di Richiamo', 'Titolo Inglese', 'Tipologia Carta']
    
    for field in field_order:
        if field in values:
            lines.append(f"{field}: {values[field]}")
    
    lines.append('---')
    return '\n'.join(lines)

def process_file(filepath):
    """Process a single file to ensure consistent YAML frontmatter"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has YAML frontmatter
        if content.startswith('---'):
            print(f"File {os.path.basename(filepath)} already has YAML frontmatter - skipping")
            return
        
        # Extract values from markdown format
        values = extract_values_from_markdown(content)
        
        # Create new YAML frontmatter
        yaml_frontmatter = create_yaml_frontmatter(values, os.path.basename(filepath))
        
        # Remove the old header lines and keep the rest of the content
        lines = content.split('\n')
        new_content_lines = []
        
        # Skip the first few lines that contain the markdown headers
        skip_lines = 0
        for i, line in enumerate(lines):
            if line.strip() and ('**_Livello' in line or '**_Costo di Richiamo_' in line):
                skip_lines += 1
            else:
                new_content_lines.extend(lines[i:])
                break
        
        # Join the content
        new_content = yaml_frontmatter + '\n\n' + '\n'.join(new_content_lines).lstrip()
        
        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Updated: {os.path.basename(filepath)}")
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

"""Main function to process all files in the abilities folder"""
folder_path = "C:/Users/gturra/DaggerHeart/La Notte Eterna C01/02_Meccaniche_DaggerHeart/Abilità"

if not os.path.exists(folder_path):
    print(f"Folder {folder_path} not found")
    sys.exit()
    
print("Processing all files in the abilities folder...")
# Process all .md files
for filename in os.listdir(folder_path):
    print(folder_path)
    if filename.endswith('.md'):
        filepath = os.path.join(folder_path, filename)
        process_file(filepath)

print("All files processed!")

# To run this script:
# 1. Save it as normalize_abilities.py
# 2. Make sure you have Python installed
# 3. Run: python normalize_abilities.py
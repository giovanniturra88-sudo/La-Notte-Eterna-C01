import os
import re

def clean_file(filepath):
    """Clean a file by keeping only the first YAML section"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all --- sections
        parts = content.split('---')
        
        if len(parts) >= 3:  # We have at least one YAML section + content + another section
            print(f"File {os.path.basename(filepath)} ha più sezioni YAML")
            
            # Keep only first YAML section and the rest of content
            # parts[0] = empty (before first ---)
            # parts[1] = first YAML content  
            # parts[2] = content after first ---
            # parts[3] = second YAML content (we want to remove this)
            
            # Rebuild: first --- + first YAML + content after first ---
            new_content = '---\n' + parts[1].strip() + '\n---\n' + parts[2].strip()
            
            # Write back to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            print(f"File pulito: {os.path.basename(filepath)}")
        else:
            print(f"File {os.path.basename(filepath)} non ha sezioni duplicate")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def main():
    """Main function to clean all files"""
    folder_path = "../02_Meccaniche_DaggerHeart/Armi_Daggerheart"
    
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} not found")
        return
    
    print("Pulizia dei file...")
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            filepath = os.path.join(folder_path, filename)
            clean_file(filepath)

if __name__ == "__main__":
    main()
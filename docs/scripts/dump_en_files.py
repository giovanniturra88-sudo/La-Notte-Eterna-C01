import os

# Folders to scan
folders = [
    '02_Meccaniche_DaggerHeart/Items/DaggerHeart',
    '02_Meccaniche_DaggerHeart/Items/DaggerHeart Hope and Fear'
]

output = []
for folder in folders:
    output.append(f'\n{"="*60}')
    output.append(f'FOLDER: {folder}')
    output.append(f'{"="*60}')
    for f in sorted(os.listdir(folder)):
        if f.endswith('.md'):
            filepath = os.path.join(folder, f)
            with open(filepath, 'r', encoding='utf-8') as fh:
                content = fh.read()
            output.append(f'\n--- FILE: {f} ---')
            output.append(content)

with open('dump_output.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))
print('Output written to dump_output.txt')

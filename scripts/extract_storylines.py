import os
from pypdf import PdfReader

base = r"c:\Users\gturra\DaggerHeart\La Notte Eterna C01\04_Risorse\Campagna\storylines"
out_dir = r"c:\Users\gturra\DaggerHeart\La Notte Eterna C01\scripts\storylines_text"
os.makedirs(out_dir, exist_ok=True)

for fn in sorted(os.listdir(base)):
    if not fn.lower().endswith(".pdf"):
        continue
    path = os.path.join(base, fn)
    try:
        reader = PdfReader(path)
    except Exception as e:
        print(f"ERROR opening {fn}: {e}")
        continue
    out = []
    for i, page in enumerate(reader.pages):
        txt = page.extract_text() or ""
        out.append(f"\n===== PAGE {i+1} =====\n{txt}")
    name = os.path.splitext(fn)[0]
    outpath = os.path.join(out_dir, name + ".txt")
    with open(outpath, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"WROTE {name}.txt  ({len(reader.pages)} pages)")

print("DONE")

import sys
from pypdf import PdfReader

path = r"c:\Users\gturra\DaggerHeart\La Notte Eterna C01\04_Risorse\Campagna\Daggerheart_HF_Full_Art_and_Printer_Friendly_Cards_-_8-14-26.pdf"
reader = PdfReader(path)
print("PAGES:", len(reader.pages))
out = []
for i, page in enumerate(reader.pages):
    txt = page.extract_text() or ""
    out.append(f"\n===== PAGE {i+1} =====\n{txt}")
with open(r"c:\Users\gturra\DaggerHeart\La Notte Eterna C01\scripts\hf_pdf_text.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("WROTE hf_pdf_text.txt")
# print first 3 pages to a quick preview
for i in range(min(3, len(reader.pages))):
    print(f"\n----- PAGE {i+1} -----")
    print((reader.pages[i].extract_text() or "")[:1500])

import fitz
import os

pdf_path = r"C:\Users\Dell 5490\Downloads\CACOSTA_U3_ACT1.COVER LETTER (1).pdf"
out_dir = r"c:\Recorrido II VR\temp_cv_images"

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

doc = fitz.open(pdf_path)
for i in range(len(doc)):
    page = doc[i]
    images = page.get_images(full=True)
    for j, img in enumerate(images):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        with open(os.path.join(out_dir, f"page_{i}_img_{j}.{image_ext}"), "wb") as f:
            f.write(image_bytes)

print(f"Extracted {len(images)} images from page {i}" if len(doc) > 0 else "")

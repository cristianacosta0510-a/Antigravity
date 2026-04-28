import fitz
from PIL import Image
import io

pdf_path = r"C:\Users\Dell 5490\Downloads\CACOSTA_U3_ACT1.COVER LETTER (1).pdf"
doc = fitz.open(pdf_path)
page = doc[1] # The cover letter is usually the second page (index 1)

# Render the page to an image
pix = page.get_pixmap(dpi=300)
img = Image.open(io.BytesIO(pix.tobytes("png")))

# Let's save the full page so I can check it exists, then we'll find the crop.
img.save(r"c:\Recorrido II VR\temp_cv_images\full_page.png")
print(f"Full page size: {img.size}")

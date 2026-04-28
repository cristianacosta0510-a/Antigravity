import base64
import re

def file_to_base64_img(file_path):
    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    ext = file_path.split('.')[-1].lower()
    return f"data:image/{ext};base64,{encoded_string}"

html_path = r"c:\Recorrido II VR\cv_template.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

logo_path = r"C:\Recorrido II VR\temp_cv_images\page_0_img_0.jpeg"
photo_path = r"C:\Recorrido II VR\temp_cv_images\page_1_img_0.jpeg"

html = html.replace('src="file:///C:/Recorrido%20II%20VR/temp_cv_images/page_0_img_0.jpeg"', f'src="{file_to_base64_img(logo_path)}"')
html = html.replace('src="file:///C:/Recorrido%20II%20VR/temp_cv_images/page_1_img_0.jpeg"', f'src="{file_to_base64_img(photo_path)}"')

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("HTML images converted to base64.")

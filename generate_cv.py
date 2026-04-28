import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Using standard fonts available in reportlab, Helvetica is very similar to Arial.
# To ensure "Arial" is used, we can load Windows Arial font.
try:
    pdfmetrics.registerFont(TTFont('Arial', 'C:\\Windows\\Fonts\\arial.ttf'))
    pdfmetrics.registerFont(TTFont('Arial-Bold', 'C:\\Windows\\Fonts\\arialbd.ttf'))
    FONT_NAME = 'Arial'
    FONT_BOLD = 'Arial-Bold'
except:
    FONT_NAME = 'Helvetica'
    FONT_BOLD = 'Helvetica-Bold'

def generate_pdf():
    pdf_path = r"C:\Users\Dell 5490\Downloads\CAcosta_U3_Act2_Curriculum_Vitae.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=72)
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    style_center = ParagraphStyle(
        'Center',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=12,
        alignment=TA_CENTER,
        leading=18 # 1.5 spacing roughly
    )
    
    style_left = ParagraphStyle(
        'Left',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=12,
        alignment=TA_LEFT,
        leading=18
    )
    
    style_justified = ParagraphStyle(
        'Justified',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=12,
        alignment=TA_JUSTIFY,
        leading=18
    )
    
    style_heading = ParagraphStyle(
        'Heading',
        parent=styles['Heading2'],
        fontName=FONT_BOLD,
        fontSize=14,
        spaceAfter=6,
        spaceBefore=12,
        textColor=colors.HexColor("#0f4c81") # A nice professional blue
    )
    
    Story = []
    
    # ==================== PAGE 1: COVER ====================
    # 1. Logo
    logo_path = r"c:\Recorrido II VR\temp_cv_images\page_0_img_0.jpeg"
    if os.path.exists(logo_path):
        img = Image(logo_path, width=150, height=150) # Adjust size
        img.hAlign = 'CENTER'
        Story.append(img)
    Story.append(Spacer(1, 40))
    
    # 2. Activity Name
    Story.append(Paragraph('"Curriculum Vitae"', style_center))
    Story.append(Spacer(1, 60))
    
    # 3. Student & Course Info
    info_text = """
    <b>Carrera:</b> Tecnologías de la Información<br/>
    <b>Grado:</b> 5to Cuatrimestre<br/>
    <b>Grupo:</b> 5C<br/>
    <b>Estudiante:</b> Christian Alejandro Acosta Perez<br/>
    <br/>
    <b>Docente:</b> Adrián López Bolaños
    """
    Story.append(Paragraph(info_text, style_left))
    
    # Spacer to push date to bottom
    Story.append(Spacer(1, 200)) # Adjust as needed
    
    # 4. Date at bottom
    Story.append(Paragraph("Morelia, Michoacán a 20 de abril de 2026", style_center))
    
    Story.append(PageBreak())
    
    # ==================== PAGE 2: CV ====================
    # Add photo to top right, name to top left. We can use a Table for layout.
    photo_path = r"c:\Recorrido II VR\temp_cv_images\page_1_img_0.jpeg"
    
    name_paragraph = Paragraph("""
    <font size="18" name="%s"><b>CHRISTIAN ALEJANDRO ACOSTA PEREZ</b></font><br/><br/>
    <font size="12">IT Developer & Technology Specialist</font>
    """ % FONT_BOLD, style_left)
    
    if os.path.exists(photo_path):
        photo_img = Image(photo_path, width=100, height=100) # Adjust size
        photo_img.hAlign = 'RIGHT'
        
        cv_header_data = [[name_paragraph, photo_img]]
        cv_header_table = Table(cv_header_data, colWidths=[350, 118])
        cv_header_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('ALIGN', (1, 0), (1, 0), 'RIGHT')
        ]))
        Story.append(cv_header_table)
    else:
        Story.append(name_paragraph)
        
    Story.append(Spacer(1, 20))
    
    # Sections as requested
    
    # 1. Datos personales
    Story.append(Paragraph('1. Personal Data', style_heading))
    personal_data = """
    <b>Address:</b> Morelia, Michoacán, Mexico<br/>
    <b>Phone:</b> +52 443 123 4567<br/>
    <b>Email:</b> christian.acosta.5c@gmail.com (simulated)
    """
    Story.append(Paragraph(personal_data, style_justified))
    
    # 2. Objetivo profesional
    Story.append(Paragraph('2. Professional Objective', style_heading))
    objective = "Motivated IT Developer and Technology Specialist seeking to leverage strong problem-solving skills and software engineering expertise to develop innovative web, VR, and XR solutions. Dedicated to continuous learning, teamwork, and contributing effectively to modern technological challenges."
    Story.append(Paragraph(objective, style_justified))
    
    # 3. Experiencia
    Story.append(Paragraph('3. Experience', style_heading))
    experience = """
    <b>VR & Web Developer (Academic Projects)</b> | Universidad Tecnológica de Morelia (2025 - 2026)<br/>
    - Developed a comprehensive "Smart City XR" web platform integrating citizen reporting using Django and Chart.js.<br/>
    - Engineered "Recorrido II VR," integrating multiple 360-degree virtual reality environments (Bosque, Catedral, San Francisco) into a unified application using A-Frame.<br/>
    - Implemented UI/UX enhancements including glassmorphism aesthetics and responsive frontend solutions.
    """
    Story.append(Paragraph(experience, style_justified))
    
    # 4. Formación
    Story.append(Paragraph('4. Education', style_heading))
    education = """
    <b>Universidad Tecnológica de Morelia (UTM)</b> - Morelia, Michoacán<br/>
    Degree: Tecnologías de la Información (Current)<br/>
    Group: 5C
    """
    Story.append(Paragraph(education, style_justified))
    
    # 5. Idiomas
    Story.append(Paragraph('5. Languages', style_heading))
    languages = """
    - <b>Spanish:</b> Native<br/>
    - <b>English:</b> Intermediate - Advanced (B2)
    """
    Story.append(Paragraph(languages, style_justified))
    
    # 6. Informática
    Story.append(Paragraph('6. IT Skills (Computing)', style_heading))
    skills = """
    - <b>Programming:</b> Python, C++, HTML5, CSS3, JavaScript.<br/>
    - <b>Technologies & Frameworks:</b> Django (ORM, templates), A-Frame (Virtual Reality), Chart.js.<br/>
    - <b>Tools & Methodologies:</b> Git, GitHub, VS Code, Agile concepts, Web Hosting.
    """
    Story.append(Paragraph(skills, style_justified))
    
    # 7. Otros datos de interés
    Story.append(Paragraph('7. Other data of interest', style_heading))
    interests = """
    - Strong passion for exploring emerging technologies like Augmented and Virtual Reality.<br/>
    - Excellent problem-solving, analytical, and teamwork capabilities.<br/>
    - Adaptable to new development environments and committed to high-quality code delivery.
    """
    Story.append(Paragraph(interests, style_justified))
    
    doc.build(Story)
    print(f"PDF generated successfully at {pdf_path}")

if __name__ == "__main__":
    generate_pdf()

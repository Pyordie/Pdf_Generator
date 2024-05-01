import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader

def generate_pdf_from_image(image_path, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    img = ImageReader(image_path)
    c.drawImage(img, 0, 0, width=letter[0], height=letter[1])
    c.save()

def generate_pdf_from_text(text_content, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    text = c.beginText(1*inch, 10.5*inch)
    text.setFont("Helvetica", 12)
    for line in text_content:
        text.textLine(line)
    c.drawText(text)
    c.save()

def main():
    file_path = input("Enter the path of the file (image or text): ")
    file_type = os.path.splitext(file_path)[1].lower()

    if file_type == '.jpg' or file_type == '.jpeg' or file_type == '.png':
        output_path = input("Enter the output PDF path: ")
        generate_pdf_from_image(file_path, output_path)
        print("PDF generated successfully!")

    elif file_type == '.txt':
        output_path = input("Enter the output PDF path: ")
        with open(file_path, 'r') as file:
            text_content = file.readlines()
        generate_pdf_from_text(text_content, output_path)
        print("PDF generated successfully!")

    else:
        print("Unsupported file format.")

if __name__ == "__main__":
    main()

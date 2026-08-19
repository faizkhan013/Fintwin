from pathlib import Path

def extract_text_from_image(file_path):
    try:
        import pytesseract
        from PIL import Image
        return pytesseract.image_to_string(Image.open(file_path))
    except Exception:
        return ""

def extract_text_from_pdf(file_path):
    try:
        import pdfplumber
        with pdfplumber.open(file_path) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    except Exception:
        return ""

import PyPDF2
import os


def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        
        for page_number in range(num_pages):
            page = reader.pages[page_number]
            text += page.extract_text()
    
    return text

# modules/pdf_reader.py

import pdfplumber
import PyPDF2


def extract_text_from_pdf(uploaded_file):
    """
    Extract text from uploaded PDF file.
    """

    text = ""

    try:
        uploaded_file.seek(0)

        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    except Exception:
        uploaded_file.seek(0)

        reader = PyPDF2.PdfReader(uploaded_file)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text.strip()
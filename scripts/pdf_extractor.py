import fitz  

def extract_text_from_pdf(pdf_file):
    try:
        with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
            text = " ".join([page.get_text() for page in doc])
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""

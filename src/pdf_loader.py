import fitz
class PDFLoader:
    @staticmethod
    def load_pdf(path):
        doc=fitz.open(path)
        text=''
        for p in doc:
            text += p.get_text()
        return text

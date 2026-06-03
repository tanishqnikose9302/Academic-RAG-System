from src.pdf_loader import PDFLoader

def test_pdf_loader():
    text = PDFLoader.load_pdf("sample.pdf")
    assert isinstance(text, str)
    assert len(text) > 0

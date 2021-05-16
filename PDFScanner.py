from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResouceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

def scan_pdf(input_pdf):
  with open(input_pdf, 'rb') as f:
    parser = PDFParser(f)
    doc = PDFDocument(parser)
    rsrcmqr = PDFResourceManager()
    device = TextConverter(rsrcmqr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmqr, device)
    

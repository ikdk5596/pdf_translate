# Extract pdf infomation for translate pdfs.
# Author : sanghong kim
# Organization : Repeblic of Korean Army
# Reference : https://realpython.com/pdf-python/

from PyPDF2 import PdfFileReader

def extract_information(pdf_path):
  with open(pdf_path, 'rb') as f:
    pdf = PdfFileReader(f)
    information = pdf.getDocumentInfo()
    number_of_pages = pdf.getNumPages()
    
  txt = f"""
  Information about {pdf_path}:
  
  Author: {information.author}
  Creator: {information.creator}
  Producer: {information.producer}
  Subject: {information.subject}
  Title: {information.title}
  Number of pages: {number_of_pages}
  """
    
  return txt, information

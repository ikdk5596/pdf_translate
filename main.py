# Extract pdf infomation for translate pdfs.
# Author : sanghong kim
# Organization : Repeblic of Korean Army
# Reference : https://realpython.com/pdf-python/

import argparse
from PyPDF2 import PdfFileReader
from extract_pdf_info import extract_information


def main(args):
  pdf_path = args.path
  
  with open(pdf_path, 'rb') as f:
    pdf = PdfFileReader(f)
    information = pdf.getDocumentInfo()
    number_of_pages = pdf.getNumPages()
    page = pdf.getPage(0)
    page_content = page.extractText()
    text = page_content # .encode('utf-8')
  
  print(text)
  

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--path', dest='path', default='sample.pdf')
  args = parser.parse_args()
  
  main(args)
  # path = 'sample.pdf'
  # txt, information = extract_information(path)
  # print(txt)

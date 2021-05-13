# Extract pdf infomation for translate pdfs.
# Author : sanghong kim
# Organization : Repeblic of Korean Army
# Reference : https://realpython.com/pdf-python/

import argparse
from PyPDF2 import PdfFileReader
import fitz
from extract_pdf_info import extract_information


def main(args):
  pdf_path = args.path
  
  with fitz.open(pdf_path) as doc:
    text = ""
    for page in doc:
      if page.getText()[-1] == 'r':
        print("enter")
      elif page.getText()[-1] == '.':
        print("end")
      # text += page.getText()
  
  print(text)
  

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--path', dest='path', default='sample.pdf')
  args = parser.parse_args()
  
  main(args)
  # path = 'sample.pdf'
  # txt, information = extract_information(path)
  # print(txt)

# Extract pdf infomation for translate pdfs.
# Author : sanghong kim
# Organization : Repeblic of Korean Army
# Reference : https://realpython.com/pdf-python/
# 이후 Regular expression을 사용하여 replace 대체
# -*- coding: UTF-8 -*-

import re
import PyPDF2
# from pdf2docx import parse
from CustomPdf2Docx.CustomPdf2Docx import parse
# from pdf2docx 
import docx
import time
import argparse
import layout_scanner
from pdfminer.pdfpage import PDFPage
from docx import Document
from google_trans_new import google_translator
import os

  
def main(args):
  input_path = args.input
  docx_path = 'temp.docx'
  output_path = args.output
  sourceLanguageCode = args.sourceLanguageCode
  targetLanguageCode = args.targetLanguageCode
 
  
  with open(input_path, 'rb') as pdf_file:
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
  if os.path.exists(output_path): os.remove(filename)
  # convert pdf 2 docx
  parse(input_path, output_path, start = 0, end = number_of_pages)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description = 'PDF to TEXT converter',
                                  prog='python -m pdf_layout_scanner')
  parser.add_argument('--input', type=str, dest='input', default='sample.pdf',
                     help='input PDF file')
  parser.add_argument('--output', type=str, dest='output', default='output.docx',
                      help='output PDF file')
  parser.add_argument('--SLC', type=str, dest='sourceLanguageCode', default='en',
                      help="Source LanguageCode")
  parser.add_argument('--TLC', type=str, dest='targetLanguageCode', default='ko',
                      help="Target LanguageCode")
  args = parser.parse_args()
  
  main(args)
  # path = 'sample.pdf'
  # txt, information = extract_information(path)
  # print(txt)

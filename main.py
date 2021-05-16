# Extract pdf infomation for translate pdfs.
# Author : sanghong kim
# Organization : Repeblic of Korean Army
# Reference : https://realpython.com/pdf-python/
# 이후 Regular expression을 사용하여 replace 대체

import re
import PyPDF2
# from pdf2docx import parse
from CustomPdf2Docx.CustomPdf2Docx import parse
# from pdf2docx 
import docx
import time
import argparse
import layout_scanner
from googletrans import Translator
from pdfminer.pdfpage import PDFPage
from translate import translate


def main(args):
  docx_path = 'temp.docx'
  input_path = args.input
  output_path = args.output
  sourceLanguageCode = args.sourceLanguageCode
  targetLanguageCode = args.targetLanguageCode
  
  with open(input_path, 'rb') as pdf_file:
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
  
  '''
  pdf_reader = PyPDF2.PdfFileReader(str(input_path))
  page = pdf_reader.getPage(0)
  print(page.mediaBox)
  '''
  parse(input_path, docx_path, start = 0, end = number_of_pages)
  
  doc = docx.Document(docx_path)
  paragraphs = [para.text for para in doc.paragraphs]
  translator = Translator()
  print(paragraphs)
  doc = docx.Document()
  '''
  for i, para in enumerate(paragraphs):
    try:
      translation = translator.translate(para,src=sourceLanguageCode,dest=targetLanguageCode)
      doc.add_paragraph(translation.text)
      time.sleep(0.1)
      print("Success "+str(i))
    except:
      print("Error "+str(i))
  doc.save(output_path)
  print("Document translation is completed.")
  '''
  

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

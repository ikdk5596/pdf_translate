# Extract pdf infomation for translate pdfs.
# Author : sanghong kim
# Organization : Repeblic of Korean Army
# Reference : https://realpython.com/pdf-python/
# 이후 Regular expression을 사용하여 replace 대체

import PyPDF2
import argparse
import layout_scanner
from pdfminer.pdfpage import PDFPage
from translate import translate


def main(args):
  input_path = args.input
  output_path = args.output
  
  pdf_reader = PyPDF2.PdfFileReader(str(input_path))
  page = pdf_reader.getPage(0)
  print(page.mediaBox)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description = 'PDF to TEXT converter',
                                  prog='python -m pdf_layout_scanner')
  parser.add_argument('--input', type=str, dest='input', default='sample.pdf',
                     help='input PDF file')
  parser.add_argument('--output', type=str, dest='output', default='output.pdf',
                      help='output PDF file')
  args = parser.parse_args()
  
  main(args)
  # path = 'sample.pdf'
  # txt, information = extract_information(path)
  # print(txt)

# Extract pdf infomation for translate pdfs.
# Author : sanghong kim
# Organization : Repeblic of Korean Army
# Reference : https://realpython.com/pdf-python/
# 이후 Regular expression을 사용하여 replace 대체

import argparse
from PyPDF2 import PdfFileReader
import fitz
from googletrans import Translator


def main(args):
  pdf_path = args.path
  translator = Translator()
  result = []
  pix = []
  
  with fitz.open(pdf_path) as doc:
    text = ""
    for page in doc:
      text += page.getText().replace("\n", "").replace("\\", "").replace(". ", ".\n")
      pix.append(page.get_pixmap())
      # text += page.getText()
      
  lines = text.splitlines()
  # print(lines)
  for line in lines:
    result.append(translator.translate(line, src='en', dest='ko'))
  
  print(result)
                  
  # print(type(text))
  # print(text)
  # print(pix)
  

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--path', dest='path', default='sample.pdf')
  args = parser.parse_args()
  
  main(args)
  # path = 'sample.pdf'
  # txt, information = extract_information(path)
  # print(txt)

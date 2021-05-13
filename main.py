import argparse
from extract_pdf_info import extract_information

def main(args):
  pdf_path = args.path
  
  txt, information, test, number_of_pages = extract_information(pdf_path)
  text = test.extractText()
  print(text.encode('utf-8')
  


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--path', dest='path', default='sample.pdf')
  args = parser.parse_args()
  
  main(args)
  # path = 'sample.pdf'
  # txt, information = extract_information(path)
  # print(txt)

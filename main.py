import argparse

def main(args):
  print(args.path)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--path', dest='path', action='store_str',
                     default='sample.pdf')
  args = parser.parse_args()
  
  main(args)
  # path = 'sample.pdf'
  # txt, information = extract_information(path)
  # print(txt)

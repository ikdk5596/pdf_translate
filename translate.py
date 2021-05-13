import fitz
from googletrans import Translator


def translate(pdf_path):
  translator = Translator()
  origin = []
  result = []
  pix = []
  
  with fitz.open(pdf_path) as doc:
    text = ""
    for page in doc:
      text += page.getText().replace("\n", "").replace("\\", "").replace(". ", ".\n")
      pix.append(page.get_pixmap())
      
  lines = text.splitlines()

  translations = translator.translate(lines, dest='ko')
  for translation in translations:
    origin.append(translation.origin)
    result.append(translation.text)
    
  return orgin, result

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParmas, LTFigure, LTTextBoxHorizontal
from pdfminer.converter import PDFPageAggregator

input = 'sample.pdf'
f = open(input, 'rb')
parser = PDFParser(f)
document = PDFDocument(parser)
if not document.is_extractable:
  raise PDFTextExtractionNotAllowed
    
rsrcmgr = PDFResourceManager()
device = PDFDevice(rsrcmgr)
  
laparams = LAParams()
  
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
  
def parse_obj(lt_objs): 
  
  for obj in lt_objs:
    if isinstance(obj, LTTextBoxHorizontal):
      print ("%6d, %6d, %s" % (obj.bbox[0], obj.bbox[1], obj.get_text().replace('\n', '_')))

    elif isinstance(obj, LTFigure):
      parse_obj(obj._objs)
      
for page in PDFPage.create_pages(document):
  interpreter.process_page(page)
  layout = device.get_result()
  
  parse_obj(layout._objs)

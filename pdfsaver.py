import PyPDF2

def save_pdf(pdf_pages, output_path):
  writer.addPage(pdf_pages)
  with open(output_path, 'wb') as output:
    writer.write(output)

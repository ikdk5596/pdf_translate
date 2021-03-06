import PyPDF2 as p
from translate import  translator
import os


filename = 'sample.pdf'
filename2 = 'output.pdf'


try:
	file = open(filename, mode = "rb")
except:
	print("File not Found, Please Enter Filename along with Directory [ex-Dowload/1.pdf]")

  
def translate():
	cur_lang = 'en'
	dest_lang = 'ko'
	try:
		data = p.PdfFileReader(file)
		print(f"Total number of pages are...{data.getNumPages()}")
	except:
		print("...Oops! Something Error While opening Pdf file")
	for page in range(data.getNumPages()):
		ok = data.getPage(int(page))
		dat = ok.extractText()
		try:
			print(f"....Translation Started....pageNo.{data.getNumPages()}")
			final_data = translator(cur_lang,dest_lang,dat)
		except:
			print("Sorry, The Translation cant happen Now.Please Try again after some Time.....")
	return final_data

if __name__ == "__main__":
	translated_pdf = translate()
	print(translated_pdf)
	finle = open(filename2+".pdf", mode="wb")
	p.PdfFileWriter.write(finle,translated_pdf)
	finle.save()
	print("Your new file is saved...")
	file.close()

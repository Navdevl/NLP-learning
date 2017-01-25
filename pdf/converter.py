from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage 
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

fp = open('resume.pdf','rb')
parser = PDFParser(fp)
document = PDFDocument(parser)
resource = PDFResourceManager()
device = PDFDevice(resource)
pagenos = set()
print pagenos
interpreter = PDFPageInterpreter(resource,device)
print (PDFPage.__doc__)
for page in PDFPage.get_pages(fp,pagenos,document):
	interpreter.process_page(page)
	print page
	print ""
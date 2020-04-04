import PyPDF2

orginal = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
merged = PyPDF2.PdfFileWriter()

for i in range(orginal.getNumPages()):
	og = orginal.getPage(i)
	wtr = watermark.getPage(0)
	og.mergePage(wtr)
	merged.addPage(og)

	with open('cloned.pdf', 'wb') as f:
		merged.write(f)







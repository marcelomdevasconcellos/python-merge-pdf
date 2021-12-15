import os
from PyPDF2 import PdfFileMerger

pdfs = os.listdir('input/')

for pdf in pdfs:
    os.rename(
    	'input/' + pdf, 
    	'input/' + pdf.replace(" ", "_"))

pdfs = os.listdir('input/')
pdfs.sort()

pdf_files = ['input/' + pdf for pdf in pdfs]

merger = PdfFileMerger()

for pdf in pdf_files:
    if '.pdf' in pdf:
        print(pdf)
        merger.append(pdf)

merger.write("output/result.pdf")
merger.close()
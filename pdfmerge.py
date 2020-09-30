import PyPDF2

from PyPDF2 import PdfFileMerger

pdfs = ['4850.pdf', '4851.pdf', '4852.pdf', '4853.pdf', '4854.pdf', '4855.pdf', '4856.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("I_485_Full.pdf")
merger.close()


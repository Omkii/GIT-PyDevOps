import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter




# print(dir(PyPDF2))
inputpdf = PdfFileReader(open("485.pdf", "rb"))


#
for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("485%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)

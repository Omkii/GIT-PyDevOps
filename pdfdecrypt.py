"""
This is to Un-Secure a PDF so that it can be split and merged.
"""
import pikepdf
pdf = pikepdf.open('I-485.pdf')
pdf.save('485.pdf')

"THE END"
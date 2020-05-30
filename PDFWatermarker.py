from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import os
import sys

operation=sys.argv[1]
pdf_file_path=sys.argv[2]
water_pdf=sys.argv[3]

def addWaterMark(pdf_file_path,water_pdf):
    template=PdfFileReader(open(pdf_file_path,'rb'))
    wtr=PdfFileReader(open(water_pdf,'rb'))
    output=PdfFileWriter()
    print(pdf_file_path)
    for i in range(template.getNumPages()):
        page=template.getPage(i)
        page.mergePage(wtr.getPage(0))
        output.addPage(page)
        
        with open('pdfFiles/watermarked.pdf','wb') as file:
            output.write(file)

def removeWaterMark(pdf_file_path):
    pass

if operation=='add':
    print(pdf_file_path)
    addWaterMark(pdf_file_path,water_pdf)
elif operation=='remove':
    removeWaterMark(pdf_file_path)
    
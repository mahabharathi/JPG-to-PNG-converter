from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import os
import sys

imputs=sys.argv[1:]

def pdfCombine(pdf_list):
    #current_directory 
    current_directory = os.getcwd()
    pdf_path=os.path.join(current_directory, 'pdfFiles\\')
    merger=PdfFileMerger()
    for pdf in pdf_list:
        print(pdf,pdf_path)
        merger.append(pdf_path+pdf)
    merger.write('pdfFiles\merged.pdf')
        
pdfCombine(imputs)
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import os



#current_directory 
current_directory = os.getcwd()
pdf_path=os.path.join(current_directory, 'pdfFiles/dummy1.pdf')

with open(pdf_path,mode='rb') as file:
    reader=PdfFileReader(file)
    print(reader.getDocumentInfo())
    page=reader.getPage(0)
    writer=PdfFileWriter()
    rotate_page=page.rotateCounterClockwise(90)
    writer.addPage(rotate_page)
    pdf_path=os.path.join(current_directory, 'pdfFiles/rotateCounterClockwise.pdf')
    with open(pdf_path,mode='wb') as new_file:
        writer.write(new_file)
        
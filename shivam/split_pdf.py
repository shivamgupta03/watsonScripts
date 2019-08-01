
import os
from PyPDF2 import PdfFileWriter, PdfFileReader

MAX_PDF_SIZE_IN_MB = 4.5

def write_file(path, initial_page, final_page):
    pdf_name = path.split('/')[-1].replace('.pdf', '')
    file_path = '/Users/shivam/myworkspace/watson/crawler/lenovo/files/hardware_manuals_split/{}_page_{}-{}.pdf'.format(pdf_name, initial_page + 1, final_page + 1)
    output = PdfFileWriter()
    inputpdf = PdfFileReader(open(path, "rb"))
    # print ('write pdf from {} to {}'.format(initial_page, final_page))
    for i in range(initial_page, final_page + 1):
        output.addPage(inputpdf.getPage(i))
    with open(file_path, "wb") as outputStream:
        output.write(outputStream)


def split_file(path):
    try:
        inputpdf = PdfFileReader(open(path, "rb"))
        initial_page = 0
        num_pages = inputpdf.numPages
        output = PdfFileWriter()
        for i in range(inputpdf.numPages):
            output.addPage(inputpdf.getPage(i))
            temp_file_path = '/Users/shivam/temppdf/tempo.pdf'
            with open(temp_file_path, "wb") as outputStream:
                output.write(outputStream)
            file_size_in_mb = os.path.getsize(temp_file_path) / (1024 * 1024.0)
            if file_size_in_mb >= MAX_PDF_SIZE_IN_MB:
                final_page = i - 1
                if initial_page == final_page:
                    print ('cannot complete: {}'.format(path))
                    return
                # print ('request for {} to {}'.format(initial_page + 1, final_page))
                write_file(path, initial_page, final_page)
                initial_page = i
                output = PdfFileWriter()
                output.addPage(inputpdf.getPage(i))
        write_file(path, initial_page, num_pages - 1)
        print ('finished: {}'.format(path))
    except Exception as e:
        print ('cannot complete: {}'.format(path))

hardware_manuals_path = '/Users/shivam/myworkspace/watson/crawler/lenovo/files/hardware_manuals'
file_names = os.listdir(hardware_manuals_path)

for file_name in file_names:
    path = '{}/{}'.format(hardware_manuals_path, file_name)
    split_file(path)


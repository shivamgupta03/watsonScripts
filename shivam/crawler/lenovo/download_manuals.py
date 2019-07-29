
# read each row of files/lenovo_hardware_manuals_path.csv
# check if the path starts with http
# check if downloaded file already exists
# download the file

import xlrd
import os
import requests
loc = ("/Users/shivam/myworkspace/watson/crawler/lenovo/files/lenovo_hardware_manuals_path.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
number_of_rows = sheet.nrows

def download_file(pdf_url, pdf_path):
    with open(pdf_path, "wb") as file:
        response = requests.get(pdf_url)
        file.write(response.content)

for i in range(number_of_rows):
    pdf_url = sheet.cell_value(i, 1)
    if not pdf_url.startswith('http'):
        continue
    pdf_name = pdf_url.split('/')[-1]
    pdf_path = 'files/hardware_manuals/{}'.format(pdf_name)
    if os.path.exists(pdf_path):
        continue
    print (pdf_url)
    download_file(pdf_url=pdf_url, pdf_path=pdf_path)

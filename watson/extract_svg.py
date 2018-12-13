"""
Use this script to extract images from a pdf when the images are in svg format
Usage:
    python extract_svg.py <path_to_pdf> <output_folder>
"""
import subprocess
import sys
import os
import PyPDF2

if __name__ == '__main__':
    try:
        pdf_filepath = sys.argv[1]
    except Exception as e:
        print("Usage: python extract_svg.py <path_to_pdf> <output_folder>")
        exit(0)

    try:
        output_folder = sys.argv[2]
    except Exception as e:
        print("No output folder specified, output defaults to current directory")
        output_folder = os.getcwd()

    # Open specified pdf file to get the number of pages
    pdf = PyPDF2.PdfFileReader(open(pdf_filepath, "rb"))
    num_pages = pdf.getNumPages()
    
    orig_dir = os.getcwd()
    pdf_filename = os.path.basename(pdf_filepath)
    folder_name = pdf_filename.replace(".pdf", "")
    folder_path = os.path.join(output_folder, folder_name)
    try:
        os.mkdir(folder_path)
    except Exception as e:
        pass

    os.chdir(folder_path)
    pdf_filepath = pdf_filepath.replace(" ", '\\ ')

    # Extract sgvs from each page in the pdf file
    for page_num in range(1, num_pages+1):
        command = "pdftocairo -f {0} -l {0} -eps {1} - | sed '/BT/,/ET/ d' > myimage-{0}.eps".format(page_num, pdf_filepath)
        print(command)
        subprocess.run(command, shell=True)

    # Convert eps files to jpgs
    for page_num in range(1, num_pages+1):
        convert_cmd = "convert myimage-{0}.eps myimage-{0}.jpg".format(page_num)
        subprocess.run(convert_cmd, shell=True)
    
    # eps files can now be deleted
    cleanup_cmd = "rm myimage-*.eps"
    subprocess.run(cleanup_cmd, shell=True)
    # Some pages will not contain images and can be deleted
    # jpg file that are smaller that 10 kilobytes (10000 bytes) are blank
    cleanup_cmd = "find . -name \"*.jpg\" -size -9999c -delete"
    os.system(cleanup_cmd)

    # navigate back to original directory
    os.chdir(orig_dir)


"""
Use this script to extract images from a pdf when the images are in jpg or png format
Usage:
    python extract_svg.py <path_to_pdf> <output_folder>
"""
import subprocess
import sys
import os 

if __name__ == '__main__':
	orig_dir = os.getcwd()
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

	pdf_filename = os.path.basename(pdf_filepath)
	folder_name = pdf_filename.replace(".pdf", "")
	folder_path = os.path.join(output_folder, folder_name)
	try:
		os.mkdir(folder_path)
	except Exception as e:
		pass

	os.chdir(folder_path)
	pdf_filepath = pdf_filepath.replace(" ", '\\ ')

	# Extract jpg and png images
	extract_cmd = "pdfimages {} image -all".format(pdf_filepath)
	print(extract_cmd)
	os.system(extract_cmd)
	
	# Images under 1 kilobye are just small icon images and can be deleted
	cleanup_cmd = "find . -name \"*.jpg\" -size -999c -delete"
	os.system(cleanup_cmd)
	cleanup_cmd = "find . -name \"*.png\" -size -999c -delete"
	os.system(cleanup_cmd)

	# navigate back to original directory
	os.chdir(orig_dir)



"""
Download images from dropbox and upload them to Watson Image Recognition
"""
import dropbox
import json
from pdf2image import convert_from_bytes
import os
from watson_developer_cloud import VisualRecognitionV3

dropbox_oauth_token = "BFlMvU8bdqcAAAAAAAAEQsl7bbgRPhTLA9VkyABAB_oIn0YhmiYbsUGAL_BdcidE"
dropbox_folder = "/Screenshots"
watson_apikey = "HUbCc2QMJXXVI0avncesA0IvuMS7raS3uwdu0xrlm30e" 

def main():
	temp_dir = create_temp_dir()
	download_from_dropbox(temp_dir)
	upload_to_watson(temp_dir)
	cleanup_temp_dir(temp_dir)

def upload_to_watson(temp_dir):
	# Uploads the JPEG images in the temp directory to Waston image recognition
	visual_recognition = VisualRecognitionV3(
    	version='2018-12-03',
    	iam_apikey=watson_apikey
	)
	for filename in os.listdir(temp_dir):
		with open(os.path.join(temp_dir, filename), 'rb') as images_file:
		    classes = visual_recognition.classify(images_file).get_result()
		    print(json.dumps(classes, indent=2))

def cleanup_temp_dir(temp_dir):
	# Clean up images files stored in temp directory
	for file in os.listdir(temp_dir):
		os.remove(os.path.join(temp_dir, file))

	os.rmdir(temp_dir)

def download_from_dropbox(temp_dir):
	# Download screenshots from dropbox
	dbx = dropbox.Dropbox(dropbox_oauth_token)
	results = dbx.files_list_folder(dropbox_folder)
	for entry in results.entries:
		files = dbx.files_list_folder(entry.path_display)
		print("Downloading and saving images from Dropbox")
		for file in files.entries:
			# Download files from dropbox
			try:
				md, res = dbx.files_download(file.path_display)
			except dropbox.exceptions.HttpError as err:
				print('*** HTTP error', err)
				return None
			# Convert PDF to JPEG
			data = convert_from_bytes(res.content)
			filename = os.path.join(temp_dir, file.name).replace(".pdf", ".jpeg")
			
			# Save images as jpeg
			for page in data:
				print(filename)
				page.save(filename, 'JPEG')

def create_temp_dir():
	# Create a temporary directory for dropbox screenshots
	temp_dir = os.path.join(os.getcwd(), "temp")
	os.mkdir(temp_dir)
	return temp_dir

if __name__ == '__main__':
	main()

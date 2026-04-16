# This function extracts a zip folder

# zip_path: path to the zip folder
# extract_to: folder where files will be extracted

import zipfile

def extract_zip_folder (zip_path, extract_to) :
 with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

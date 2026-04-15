# This function copies the text file (.txt) from the source folder to the destination folder

# source_folder: path to the source folder
# dest_folder: path to the destination folder
# text_file_names: list of text file names to be copied

import os
import shutil

def copy_text_file_from_source_folder_2_dest_folder (source_folder, dest_folder, text_file_names):
 
 os.makedirs(dest_folder, exist_ok=True)

 for f in text_file_names:
    src = os.path.join(source_folder, f)
    dst = os.path.join(dest_folder, f)

    if os.path.exists(src):
        shutil.copy2(src, dst)
    else:
        print(f"File not found: {src}")

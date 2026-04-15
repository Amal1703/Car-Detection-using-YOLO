# This function copies the images from the source folder to the destination folder

# source_folder: path to the source folder
# dest_folder: path to the destination folder
# image_filenames: list of image filenames to be copied

import os

def copy_image_from_source_folder_2_dest_folder (source_folder, dest_folder, image_filenames):

 os.makedirs(dest_folder, exist_ok=True)

 for img in image_filenames:
    src_path = os.path.join(source_folder, img)
    dst_path = os.path.join(dest_folder, img)

    if os.path.exists(src_path):
        shutil.copy(src_path, dst_path)
       # print(f"Copied image: {img}")
    else:
        print(f"Image not found: {img}")

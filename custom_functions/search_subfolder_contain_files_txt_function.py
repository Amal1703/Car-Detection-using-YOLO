# This function finds the subfolder that contains the files.txt (corresponding to YOLO annotations)

# path_main_folder: path of the main folder

from pathlib import Path

def search_subfolder_contain_files_txt (path_main_folder) :

 base_path = Path(path_main_folder)

 for subfolder in base_path.rglob("*"):
    if subfolder.is_dir():
        files = list(subfolder.iterdir())

        # check: subfolder is not empty and all files are .txt
        if files and all(f.is_file() and f.suffix == ".txt" for f in files):
           # print(subfolder)
            break
            
 return str(subfolder)

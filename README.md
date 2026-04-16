# Car-Detection-using-YOLO

Objectif: Detect Acura Integra Type R 2001, Acura TL Sedan 2012, and Acura RL Sedan 2012 car images using YOLO.

Dataset (car images): The image data I found is from this URL: "https://www.kaggle.com/datasets/jutrera/stanford-car-dataset-by-classes-folder". This URL contains other car datasets as well, separated into train and test folders. 
In this project, I grouped those two folders together.

Annotation: I used Make Sense software to annotate the images. You can find it at: "https://www.makesense.ai/". After annotation, we can export:
  - A folder containing YOLO annotations
  - A CSV file containing image names and bounding boxes
  - A folder containing XML files

Car_data folder: A folder that contains car images for the 3 classes

Custom_function: Contains .py files which correspond to functions used in the main Jupyter notebook

Car-Detection-using-YOLO.ipynb: The main Jupyter notebook file

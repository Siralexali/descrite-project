from PIL import Image
import numpy as np
import os
from os import listdir


folder_dir = (r"C:\Users\PARDIS\Desktop\uni\discrete\project\project_descrite\Picture")
for files in os.listdir(folder_dir):
    folder_dir = (r"C:\Users\PARDIS\Desktop\uni\discrete\project\project_descrite\Picture")
    folder_dir = (r"C:\Users\PARDIS\Desktop\uni\discrete\project\project_descrite\Picture" + '\\' + files)
    for images in os.listdir(folder_dir):
        if (images.endswith(".png")) or (images.endswith(".jpg")) or (images.endswith(".jpeg")) or (images.endswith(".jfif")):
            images = Image.open((folder_dir+'\\'+images))
            images = images.convert('L')
            arrimage = np.asarray(images)
            arrimage = arrimage.flatten()

            print(arrimage,len(arrimage))
#!/usr/bin/env python3
import os
from PIL import Image

#open images in directory and convert them from RGBA to RGB

images_path =  'c:/Users/Miro/My Drive/Python_coursera/7 Final project/catalog_information/supplier-data/images/'
images_outpath = 'c:/Users/Miro/My Drive/Python_coursera/7 Final project/catalog_information/supplier-data/images/'

def convert_rgb(images_path):

    # Check whether the outpath exists or no
    isExist = os.path.exists(images_outpath)

    if not isExist:
  
    # Create a new directory because it does not exist 
        os.makedirs(images_outpath)
        print("The new directory is created!")

    
    for images in os.listdir(images_path):
        #imagePath contains name of the image 
        inputpath = os.path.join(images_path, images)


        #inputPath contains the full directory name
        img = Image.open(inputpath).convert('RGB')

        #convert .tiff to .jpeg
        fullOutPath = os.path.join(images_outpath, images + '.jpeg')

        #remove .tiff from the file name
        replace_name = fullOutPath.replace('.tiff', '')
        #fullOutPath contains the path of the output
        #image that needs to be generated
        img.resize((600,400)).save(replace_name) 


convert_rgb(images_path)



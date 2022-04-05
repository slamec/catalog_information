#!/usr/bin/env python3
import requests
import os
import glob
from PIL import Image

# loop over files in images path and send them to server, open only .jpeg files

url = "http://localhost:8000/" # needs to be changed based on server url
images_path =  'c:/Users/Miro/My Drive/Python_coursera/7 Final project/catalog_information/supplier-data/images/*.jpeg'

for images in glob.glob(images_path):

    input_path = os.path.join(images_path, images)

    print(input_path)

    with open(input_path, "rb") as opened:

        r = requests.post(url, files={'file': opened})





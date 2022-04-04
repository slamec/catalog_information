#!/usr/bin/env python3
import requests
import os
import glob

# This example shows how a file can be uploaded using
# The Python Requests module

# url = "http://localhost/upload/"
# with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
#     r = requests.post(url, files={'file': opened})


# loop over files in images path and send them to server, open only .jpeg files

images_path =  'c:/Users/Miro/My Drive/Python_coursera/7 Final project/catalog_information/supplier-data/images/*.jpeg'

for images in glob.glob(images_path):
    print(images)



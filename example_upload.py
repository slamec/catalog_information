#!/usr/bin/env python3
import requests


images_path =  'c:/Users/Miro/My Drive/Python_coursera/7 Final project/catalog_information/supplier-data/images/'

url = "http://localhost/upload/"
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})




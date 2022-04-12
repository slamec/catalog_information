# !/usr/bin/env python3

from importlib.metadata import files
import os
import requests
import glob
import json                            

text_path = 'c:/Users/Miro/My Drive/Python_coursera/7 Final project/catalog_information/supplier-data/descriptions/*.txt'
text_path_dir = 'c:/Users/Miro/My Drive/Python_coursera/7 Final project/catalog_information/supplier-data/descriptions/'


def product_information(text_path):
    fruit_information = {}

    for items in os.listdir(text_path_dir):
        files_dir = items

    for files in glob.glob(text_path):
        fruit_information.clear()

        input_path = os.path.join(text_path, files)
    
            
        with open(input_path, 'r') as opened:
            texts = opened.read().splitlines()

            fruit_information['name'] = texts[0]
            fruit_information['weight'] = texts[1].replace('lbs', '')
            fruit_information['description'] = texts[2].replace('Â\xa0', '')
            fruit_information['image_name'] = (files_dir.strip('.txt')) + '.jpeg' #should print only file name
            print(fruit_information)
    
    return 0
    

product_information(text_path)

print(json.dumps(product_information(text_path), indent = 4))

    




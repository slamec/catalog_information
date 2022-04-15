# !/usr/bin/env python3

from textwrap import indent
import reportlab
import os 
import json

text_path = 'c:/Users/Miro/My Drive/Python_coursera/7 Final project/catalog_information/supplier-data/descriptions/'

def product_information(text_path):
    """This function loop over .txt files in given directory and convert them to dictionary in format: name, weight, description and image name also uploads json file made from dict to a server"""
    fruit_information = {}

    for files in os.listdir(text_path):
        fruit_information.clear()

        input_path = os.path.join(text_path, files)

    
        with open(input_path,  'r') as opened:
            texts = opened.read().splitlines()
            

            fruit_information['name'] = texts[0]
            fruit_information['weight'] = texts[1].replace('lbs', '')
            fruit_information['description'] = texts[2].replace('Â\xa0', '')
            fruit_information['image_name'] = (files.strip('.txt')) + '.jpeg' 

        print(fruit_information)

    return 0

product_information(text_path)
print(json.dumps(product_information(text_path), indent = 4))


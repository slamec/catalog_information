# !/usr/bin/env python3

from textwrap import indent
import reportlab
import os 
import json

text_path = 'c:/Users/Miro/My Drive/Python_coursera/7 Final project/catalog_information/supplier-data/descriptions/'


fruit_information = {}
list_dict = []
    
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


    for k in fruit_information.items():
        list_dict.append({k})

# print(list_dict)

with open('fruit.json', 'w') as file:
    json.dump(fruit_information, file)



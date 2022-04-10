# !/usr/bin/env python3

import os
import requests
import glob                             

text_path = 'c:/Users/Miro/My Drive/Python_coursera/7 Final project/catalog_information/supplier-data/descriptions/*.txt'



def product_information(text_path):

    fruit_information = {}

    for files in glob.glob(text_path):

        input_path = os.path.join(text_path, files)

        with open(input_path, 'r') as opened:
            texts = opened.read().splitlines()

            fruit_information['name'] = texts[0]
            fruit_information['weight'] = texts[1].replace('lbs', '')
            fruit_information['description'] = texts[2].replace('Â\xa0', '')
            #fruit_information['image_name'] = input_path.split('.') + '.jpeg'

            return fruit_information

print(product_information(text_path))




# !/usr/bin/env python3

import os
import requests
import glob                             

text_path = 'c:/Users/Miro/My Drive/Python_coursera/7 Final project/catalog_information/supplier-data/descriptions/*.txt'

def product_information(text_path):

    fruit_information_list = []

    for files in glob.glob(text_path):

        input_path = os.path.join(text_path, files)

        with open(input_path, 'r') as opened:
            texts = opened.read().splitlines()

            fruit_information_list.append(texts)

    return fruit_information_list


def product_dict():

    fruit_information = {}


    for items in product_information(text_path):

        fruit_information['name'] = items[0]
        fruit_information['weight'] = items[1]
        fruit_information['description'] = items[2]
    
    return fruit_information

print(product_dict())
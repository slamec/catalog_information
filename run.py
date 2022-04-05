# !/usr/bin/env python3

import os
import requests
import glob                             

text_path = 'c:/Users/Miro/My Drive/Python_coursera/7 Final project/catalog_information/supplier-data/descriptions/*.txt'

fruit_information_list = []
fruit_information = {}

for files in glob.glob(text_path):

    input_path = os.path.join(text_path, files)

    with open(input_path, 'r') as opened:
        texts = opened.read().splitlines()

        fruit_information_list.append(texts)

for items in fruit_information_list:

    # fruit_information[items[0]] = 'name'

    fruit_information[items[0]] = 'name'
    fruit_information[items[1]] = 'weight'
    fruit_information[items[2]] = 'description'


new_dict = {}
for k, v in fruit_information.items():
    new_dict[v] = k

print(new_dict)
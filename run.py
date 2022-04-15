# !/usr/bin/env python3

from importlib.metadata import files
import os
import requests
import json                            

text_path = 'c:/Users/Miro/My Drive/Python_coursera/7 Final project/catalog_information/supplier-data/descriptions/'
url = 'localhost:8000' # server url has to be changed


def product_information(text_path, url):
    """This function loop over .txt files in given directory and convert them to dictionary in format: name, weight, description and image name also uploads json file made from dict to a server"""
    fruit_information = {}


    for files in os.listdir(text_path):
        fruit_information.clear()

        input_path = os.path.join(text_path, files)
    
            
        with open(input_path, 'r') as opened:
            texts = opened.read().splitlines()

            fruit_information['name'] = texts[0]
            fruit_information['weight'] = texts[1].replace('lbs', '')
            fruit_information['description'] = texts[2].replace('Â\xa0', '')
            fruit_information['image_name'] = (files.strip('.txt')) + '.jpeg' 
            print(fruit_information)

            if url != '':
                response = requests.post(url, json = fruit_information)
                print(response.request.url)
                print(response.status_code)

    return 0
    
product_information(text_path, url)
print(json.dumps(product_information(text_path, url), indent = 4))




    




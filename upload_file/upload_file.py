#!/usr/bin/env python3

#TODO write tests
import requests

url = "https://api.metadefender.com/v4/file/bzIxMDMwNi00VS0wY2VFV3ZhaUc4Nnk5TkU"

headers = {
    'apikey': 
}

response = requests.request("GET", url, headers=headers)

print(response.text)

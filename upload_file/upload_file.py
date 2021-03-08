#!/usr/bin/env python3



url = "https://api.metadefender.com/v4/file/" #id for a test? bzIxMDMwNi00VS0wY2VFV3ZhaUc4Nnk5TkU

headers = {
    'apikey': #do not fill out! must read from the cli or a file...
}

response = requests.request("GET", url, headers=headers)

print(response.text)

if __name__ == '__main__':
    

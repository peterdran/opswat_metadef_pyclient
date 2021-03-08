#!/usr/bin/env python3
import sys


url = "https://api.metadefender.com/v4/file/" #file id for a test? bzIxMDMwNi00VS0wY2VFV3ZhaUc4Nnk5TkU

headers = {
    'apikey': #do not fill out! must read from the cli or a file...else brain damage occurs and have to start over
}

response = requests.request("GET", url, headers=headers)

print(response.text)

if __name__ == '__main__':
    #(pre-task) handle args
    arg_name_str = #TODO whatever the arg thingy is
    #open file
    
    #compute hash
    file_sha256_str = 
    #lookup hash via API
    #logic fork: if found show results via id else
    #upload file via API
    #poll for progress via API
    #show results via new id

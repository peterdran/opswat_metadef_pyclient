#!/usr/bin/env python3
import sys

import file_helper
import api_interface

def result_formatter(json_obj):
    return None

if __name__ == '__main__':
    #(pre-task) handle args
    try:
        arg_name_str = sys.argv[1]
    except IndexError:
        print("No filename passed")
        sys.exit(1)
    
    #(pre-task) get api key from a keyfile TODO document
    try:
        api_key_str = file_helper.open_arbitrary_file("../keyfile", "r").splitlines()[0]
    except FileNotFoundError:
        print("API keyfile not found. Please supply a keyfile?")
        sys.exit(3)
    
    #print(api_key_str)
    #open file
    try:
        input_file_bin = file_helper.open_arbitrary_file(arg_name_str, "rb")
    except FileNotFoundError:
        print("File not found.")
        sys.exit(2)
    
    #compute hash
    file_sha256_str = file_helper.hash_file(input_file_bin).hexdigest()
    #print(file_sha256_str)
    
    metadef_file = api_interface.MetadefFile(api_key_str, arg_name_str, file_sha256_str, input_file_bin)
    
    #lookup hash via API
    hash_exists_bool = metadef_file.hash_exists_remotely()
    
    #logic fork: if found show results via id else
    if not hash_exists_bool:
        #upload file via API
        metadef_file.upload_file()
        #poll for progress via API
        
    
    metadef_file.show_last_response()
    #show results via new id


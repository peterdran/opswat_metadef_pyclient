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
    
    #(pre-task) get api key somehow
    try:
        api_key_str = get_api_key("keyfile", "r")
    except:
        print("API keyfile not found. Please supply a keyfile?")
        sys.exit(3)
    
    #open file
    try:
        input_file_bin = file_helper.open_arbitrary_file(arg_name_str, "rb")
    except:
        print("File not found.")
        sys.exit(2)
    
    #compute hash
    file_sha256_str = file_helper.hash_file(arg_name_str)
    
    #lookup hash via API
    hash_exists_bool = api_interface.metadef_api_lookup_by_hash(hash_str, api_key)
    
    #logic fork: if found show results via id else
    #if not hash_exists_bool:
        
        #upload file via API
        #poll for progress via API
    
    #show results via new id


#!/usr/bin/env python3
import sys

import file_helper
import api_interface

def result_formatter(json_obj):
    

if __name__ == '__main__':
    #(pre-task) handle args
    #(pre-task) get api key somehow
    arg_name_str = #TODO whatever the arg thingy is
    #open file
    input_file_bin = file_helper.open_arbitrary_file(arg_name_str)
    
    #compute hash
    file_sha256_str = file_helper.hash_file(arg_name_str)
    #lookup hash via API
    
    #logic fork: if found show results via id else
    #upload file via API
    #poll for progress via API
    #show results via new id

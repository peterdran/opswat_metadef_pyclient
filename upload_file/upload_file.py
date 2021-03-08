#!/usr/bin/env python3
import sys

if __name__ == '__main__':
    #(pre-task) handle args
    arg_name_str = #TODO whatever the arg thingy is
    #open file
    input_file_bin = open_arbitrary_file(arg_name_str)
    
    #compute hash
    file_sha256_str = hash_file(arg_name_str)
    #lookup hash via API
    
    #logic fork: if found show results via id else
    #upload file via API
    #poll for progress via API
    #show results via new id

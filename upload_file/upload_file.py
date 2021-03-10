#!/usr/bin/env python3
import sys
import time

import requests

import file_helper
import api_interface


def result_formatter(dict_obj):
    """Formats and prints the scan results to be readable for humans"""
    print("filename:", dict_obj['file_info']['display_name'])
    print("overall_status:", dict_obj['scan_results']['scan_all_result_a'])
    
    scan_body_resp = dict_obj['scan_results']['scan_details']
    for engine in scan_body_resp:
        print('\nengine:', engine)
        for engine_results in scan_body_resp[engine]:
            raw_engine_result_val = scan_body_resp[engine][engine_results]
            if engine_results != "scan_time":
                if engine_results == "threat_found" and raw_engine_result_val == "":
                    formatted_string_val = "Clean"
                else:
                    formatted_string_val = raw_engine_result_val
                print(engine_results,":", formatted_string_val)


if __name__ == '__main__':
    try:
        arg_name_str = sys.argv[1]
    except IndexError:
        print("No filename passed")
        sys.exit(1)
    
    #(pre-task) get api key from a keyfile TODO document
    try:
        api_key_str = file_helper.open_arbitrary_file("keyfile", "r").splitlines()[0]
    except FileNotFoundError:
        print("API keyfile not found. Please supply a keyfile?")
        sys.exit(3)
    
    try:
        input_file_bin = file_helper.open_arbitrary_file(arg_name_str, "rb")
    except FileNotFoundError:
        print("File not found.")
        sys.exit(2)
    
    file_sha256_str = file_helper.hash_file(input_file_bin)
    
    metadef_file = api_interface.MetadefFile(api_key_str,
                                             arg_name_str,
                                             file_sha256_str,
                                             input_file_bin)
    
    try:
        hash_exists_bool = metadef_file.hash_exists_remotely()
    except requests.exceptions.ConnectionError:
        print("Network error on requesting hash from API")
        sys.exit(4)
    
    if not hash_exists_bool:
        try:
            print(metadef_file.upload_file())
        except requests.exceptions.ConnectionError:
            print("Network error on uploading file")
            sys.exit(4)
    
        scannning_is_done = False
        while not scannning_is_done:
            try:
                scannning_is_done = metadef_file.query_progress()
            except requests.exceptions.ConnectionError:
                print("Network error on querying progress")
            finally:
                time.sleep(1)
        
    result_body = metadef_file.show_last_response()
    result_formatter(result_body)


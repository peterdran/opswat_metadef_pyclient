import requests


def metadef_api_lookup_by_hash(hash_str, api_key):
    api_url_str = "https://api.metadefender.com/v4/"
    headers = {
    'apikey': api_key
    }
    
    
    #TODO try..get this statement
    response = requests.request("GET", api_url_str, headers=headers)

def metadef_api_upload_file(file_content_bin, file_name_str, api_key):
    api_url_str = "https://api.metadefender.com/v4/"
    headers = {
    'apikey': api_key
    }
    
    
    #TODO try..get this statement
    response = requests.request("GET", api_url_str, headers=headers)

def metadef_api_query_file_results(file_id_str, api_key):
    
    api_url_str = "https://api.metadefender.com/v4/file/" + file_id_str #TODO use template method to prevent code execution
    #file id for a test? bzIxMDMwNi00VS0wY2VFV3ZhaUc4Nnk5TkU
    
    headers = {
    'apikey': api_key #do not fill out! must read from the cli or a file...else brain damage occurs and have to start over
    }
    #TODO try..get this statement
    response = requests.request("GET", api_url_str, headers=headers) #generic response, modify to suit needs
    

def metadef_api_progress_poll(file_id_str):
    api_url_str = "https://api.metadefender.com/v4/"
    headers = {
    'apikey': api_key
    }
    
    #TODO try..get this statement
    response = requests.request("GET", api_url_str, headers=headers)
    


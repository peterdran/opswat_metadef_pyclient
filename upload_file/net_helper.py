import requests

url = "https://api.metadefender.com/v4/file/" #file id for a test? bzIxMDMwNi00VS0wY2VFV3ZhaUc4Nnk5TkU

headers = { #TODO NOT A GLOBAL!!!
    'apikey': #do not fill out! must read from the cli or a file...else brain damage occurs and have to start over
}

response = requests.request("GET", url, headers=headers) #generic response, modify to suit needs

print(response.text)

def metadef_api_lookup_by_hash(hash_str):
    return None

def metadef_api_upload_file(file_content_bin, file_name_str):
    return None

def metadef_api_query_file_results(file_id_str):
    return None

def metadef_api_progress_poll(file_id_str):
    return None

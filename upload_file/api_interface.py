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
    
    
    
    
    
    
    
class MetadefAPI:
    base_api_string = "https://api.metadefender.com/v4/"
    
    def __init__(self, endpoint_uri, api_key):
        self.endpoint_uri = endpoint_uri
        self._api_key = api_key
    
    def call_api(api_operation, parameters=""):
        pass
    
    #TODO what methods would work best here?

class MetadefFile(MetadefAPI)
    
    def __init__(self, file_name, file_hash, file_data)
        super().__init__("MetadefAPI")
        self.file_name = file_name
        self.file_hash = file_hash
        self.file_data = file_data
        #self.file_attributes = None
    
    def lookup_by_hash():
        return self.file_hash  #TODO clarify scope of method
    
    def upload_file():
        
    
    def query_file():
        
    
    def query_progress():
        
    
    

import requests

class MetadefAPI:
    base_api_string = "https://api.metadefender.com/v4/"
    
    def __init__(self, endpoint_uri, api_key):
        self.endpoint_uri = endpoint_uri
        self.api_key = api_key
    
    def call_api(api_operation, parameters=""):
        pass
    
    #TODO what methods would work best here?

class MetadefFile(MetadefAPI):
    
    def __init__(self, api_key, file_name, file_hash, file_data, file_remote_id):
        super().__init__("file/", api_key)
        self.file_name = file_name
        self.file_hash = file_hash
        self.file_data = file_data
        self.file_remote_id = file_remote_id
        #self.file_attributes = None
    
    def lookup_by_hash():
        if self.file_response is None:
            if self.file_hash is not None:
                self.endpoint_uri = self.base_api_string + "hash/" + self.file_hash #TODO use string templates to prevent code execution
                
                headers = {
                'apikey': self.api_key
                }
                #TODO try..get this
                self.file_response = requests.request("GET", api_url_str, headers=headers)
            else:
                #TODO throw exception
        return 
    
    def hash_exists_remotely():
        self.lookup_by_hash()
        #logic goes here
    
    def upload_file():
        if self.hash_response is not None:
            self.endpoint_uri = self.base_api_string + "file/" #TODO use string templates to prevent code execution
            
            headers = {
                'apikey': self.api_key,
                'content-type': 'application/octet-stream'
            }
            
            #TODO where to store this response?
            requests.request("GET", api_url_str, headers=headers)
        else
            #don't?
        return
    
    def query_file():
        if self.file_remote_id is not None:
            self.endpoint_uri = self.base_api_string + "file/" + self.file_remote_id #TODO use string templates to prevent code execution
            
            headers = {
            'apikey': self.api_key
            }
            #TODO try..get this
            self.file_response = requests.request("GET", api_url_str, headers=headers)
        else:
            #TODO throw exception
        return 
    
    def query_progress():
        pass
    
    











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
    
    
    
    
    
    
    


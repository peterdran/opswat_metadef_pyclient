import requests

class MetadefAPI:
    BASE_API_STRING = "https://api.metadefender.com/v4/"
    
    def __init__(self, api_key):
        #self.endpoint_uri = None
        self.api_key = api_key
    
    def call_api(api_operation, parameters=""):
        pass
    
    #TODO what methods would work best here (if any?)

class MetadefFile(MetadefAPI):
    
    def __init__(self, api_key, file_name, file_hash, file_data, file_remote_id):
        super().__init__(api_key)
        self.file_name = file_name
        self.file_hash = file_hash
        self.file_data = file_data
        self.file_remote_id = file_remote_id
    
    def __init__(self, api_key, file_name, file_hash, file_data):
        super().__init__(api_key)
        self.file_name = file_name
        self.file_hash = file_hash
        self.file_data = file_data
        self.file_remote_id = None
        self.file_response = None
        #maybe a in_progress boolean?
    
    def lookup_by_hash(self):
        if self.file_response is None:
            if self.file_hash is not None:
                endpoint_uri = self.BASE_API_STRING + "hash/" + self.file_hash #TODO use string templates to prevent code execution
                
                headers = {
                'apikey': self.api_key
                }
                #TODO try..get this
                self.file_response = requests.request("GET", endpoint_uri, headers=headers)
            else:
                pass#TODO throw exception
        return
    
    def hash_exists_remotely(self):
        print(self.lookup_by_hash())
        #logic to return a boolean goes here
    
    def upload_file(self):
        if self.hash_response is not None:
            endpoint_uri = self.BASE_API_STRING + "file/" #TODO use string templates to prevent code execution
            
            headers = {
                'apikey': self.api_key,
                'content-type': 'application/octet-stream'
            }
            
            #TODO where to store this response?
            requests.request("GET", endpoint_uri, headers=headers)
        else:
            pass #don't?
        return
    
    def query_file(self):
        if self.file_remote_id is not None:
            self.query_progress()
        else:
            pass #TODO throw exception
        return
    
    def query_progress(self):
        endpoint_uri = self.BASE_API_STRING + "file/" + self.file_remote_id #TODO use string templates to prevent code execution
        
        headers = {
        'apikey': self.api_key
        }
        #TODO try..get this
        self.file_response = requests.request("GET", endpoint_uri, headers=headers)
        return
    def show_last_response(self):
        return self.file_response



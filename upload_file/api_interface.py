import requests

class MetadefAPI:
    BASE_API_STRING = "https://api.metadefender.com/v4/"
    
    def __init__(self, api_key):
        #self.endpoint_uri = None
        self.api_key = api_key
    

class MetadefFile(MetadefAPI):
    
    def __init__(self):
        super().__init__(None)
        self.file_name = None
        self.file_hash = None
        self.file_data = None
        self.file_remote_id = None
        self.file_response = None
    
    def __init__(self, api_key, file_name, file_hash, file_data):
        super().__init__(api_key)
        self.file_name = file_name
        self.file_hash = file_hash
        self.file_data = file_data
        self.file_remote_id = None
        self.file_response = None
        #maybe a in_progress boolean?
    """TODO rest of docstring; returns: HTTP status code"""
    def lookup_by_hash(self):
        if self.file_hash is not None:
            endpoint_uri = self.BASE_API_STRING + "hash/" + self.file_hash #TODO use string templates to prevent code execution
            
            headers = {
            'apikey': self.api_key
            }
            #TODO try..get this
            self.file_response = requests.get(endpoint_uri, headers=headers)
            self.file_response.raise_for_status()
            return self.file_response.status_code
            #return requests.request("GET", endpoint_uri, headers=headers)
        else:
            #raise ArgumentError
            pass
        return
    
    def hash_exists_remotely(self):
        try:
            self.lookup_by_hash()
        except requests.exceptions.HTTPError:
            return False
        return True
    
    def upload_file(self):
        #if not self.hash_exists_remotely(): #TODO Refactor this spaghetti
        endpoint_uri = self.BASE_API_STRING + "file/" #TODO use string templates to prevent code execution
        
        headers = {
            'apikey': self.api_key,
            'filename': self.file_name,
            'content-type': 'application/octet-stream'
        }
        
        #TODO where to store this response?
        self.file_response = requests.post(endpoint_uri, headers=headers, data=self.file_data).json()
        #else:
        #    pass #don't?
        self.file_response.raise_for_status()
        return self.file_response.status_code
    
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
        self.file_response = requests.get(endpoint_uri, headers=headers)
        return
    
    def show_last_response(self):
        return self.file_response.json()



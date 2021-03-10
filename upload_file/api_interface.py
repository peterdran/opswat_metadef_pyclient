import requests

class MetadefAPI:
    """Metadefender API base class. Intended to be inherited by other,
    functionality-specific classes"""
    BASE_API_STRING = "https://api.metadefender.com/v4/"
    def __init__(self, api_key):
        """Constructor for the base Metadefender Cloud API. 
        Requires the user's API key."""
        self.api_key = api_key


class MetadefFile(MetadefAPI):
    """MetaDefender API file scanning client class.
    Handles basic scanning functionality ATM."""
    def __init__(self, api_key, file_name, file_hash, file_data):
        """Constructor for a Metadefender Cloud File submission.
        Requires the file name, data, and hash (MD5, SHA1, or SHA-256)
        in addition to the user's API key."""
        super().__init__(api_key)
        self.file_name = file_name
        self.file_hash = file_hash
        self.file_data = file_data
        self.file_remote_id = None
        self.file_response = None
        self.file_progress = None
    
    def lookup_by_hash(self):
        """Looks up local file by stored MD5, SHA1, or SHA-256 hash;
        Returns: the file_id stored on the server,
        raises "requests.exceptions.HTTPError" if not found on the server"""
        if self.file_hash is not None:
            #TODO use string templates to prevent code execution
            endpoint_uri = self.BASE_API_STRING + "hash/" + self.file_hash
            
            headers = {
            'apikey': self.api_key
            }
            
            self.file_response = requests.get(endpoint_uri, headers=headers)
            self.file_response.raise_for_status()
            self.file_remote_id = self.file_response.json()['data_id']
            return self.file_remote_id
        return
    
    def hash_exists_remotely(self):
        """Tests if the file's hash exists on the API server.
        Returns a boolean, indicating existence with True.
        Handles HTTP errors, but passes network exceptions due to ambiguous results"""
        try:
            self.lookup_by_hash()
        except requests.exceptions.HTTPError:
            return False
        return True
    
    def upload_file(self):
        """Uploads the file to the server. Returns the file id on the API server.
        Raises standard HTTP and Network errors."""
        endpoint_uri = self.BASE_API_STRING + "file/"
        
        headers = {
            'apikey': self.api_key,
            'filename': self.file_name,
            'content-type': 'application/octet-stream'
        }
        
        self.file_response = requests.post(endpoint_uri,
                                           headers=headers,
                                           data=self.file_data)
        self.file_response.raise_for_status()
        self.file_remote_id = self.file_response.json()['data_id']
        
        return self.file_remote_id
    
    def query_progress(self):
        """Checks progress of a scan on the server.
        Returns a boolean indicating scan completion with True.
        Raises standard HTTP and Network errors."""
        endpoint_uri = self.BASE_API_STRING + "file/" + self.file_remote_id
        
        headers = {
        'apikey': self.api_key
        }
        
        self.file_response = requests.get(endpoint_uri, headers=headers)
        self.file_response.raise_for_status()
        
        progress_stat = self.file_response.json()['scan_results']['progress_percentage']
        print("Progress %:", progress_stat)
        if progress_stat < 100:
            return False
        return True
    
    def show_last_response(self):
        """Returns the last stored result,
        conveniently converted to python's dict format from JSON"""
        return self.file_response.json()


from hashlib import sha256

"""Opens any file as a binary blob and returns a python object. 
Returns the file's contents depending on the read_type. 
See python's open() function documentation for more information."""
def open_arbitrary_file(file_name, read_type):
    with open(file_name, mode=read_type) as file_object:
        arb_file = file_object.read()
        file_object.close()
    
    return arb_file

"""Wrapper around hashlib's sha256 function to return a usable hash string."""
def hash_file(file_bytes_object):
    return sha256(file_bytes_object).hexdigest()



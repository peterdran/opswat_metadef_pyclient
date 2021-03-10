from hashlib import sha256

""" Opens any file as a binary blob and returns a python object"""
def open_arbitrary_file(file_name, read_type):
    #arb_file = None
    
    with open(file_name, mode=read_type) as file_object:
        arb_file = file_object.read()
        file_object.close()
    
    return arb_file

def hash_file(file_bytes_object):
    return sha256(file_bytes_object)



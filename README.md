# OPSWAT Metadefender python client
##### opswat_metadef_pyclient
## Peter Dranishnikov
---

#### Overview

The program tests the provided file against MedaDefender Cloud's API service. 
The program is written in python 3. 
An API key from MedaDefender Cloud is required to be placed into a keyfile (see the Installation section below). 

```
python3 upload_file/upload_file.py [FILE]
```

`python` may be used if aliased for python version 3. Operation of the program in python version 2 is not guaranteed. 

`[FILE]`: The file to be examined. Any file type is acceptable. 
Repeat program operation with the same file will not reupload the file after subsequent runs. 

#### Installation
The program assumes that python3 and the requests library are installed. 

```
git clone https://github.com/peterdran/opswat_metadef_pyclient.git
cd opswat_metadef_pyclient

touch keyfile
#insert api key into the keyfile somehow

python3 upload_file/upload_file.py [FILE]
```

#### Known Issues
* When using relative file paths and the file upload is performed, the full path name is used instead of the base file name. 
* If python code is in the file name, then python code execution is theoretically possible. This bug has not been thoroughly tested. 
* The keyfile name and location cannot be changed. 



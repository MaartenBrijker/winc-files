__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile

def clean_cache():
    cwd = os.getcwd()
    path = cwd + '/files/cache'
    try: 
        os.mkdir(path) 
    except: 
        for file_name in os.listdir(path):
            file = path + '/' + file_name
            if os.path.isfile(file):
                os.remove(file)  
             
def cache_zip(zip_path, cache_path):
    clean_cache()
    with ZipFile(zip_path, 'r') as zipObj:
        zipObj.extractall(path=cache_path)

def cached_files():
    cwd = os.getcwd()
    path = cwd + '/files/cache'
    abs_path = os.path.abspath(path)
    if (os.path.exists(abs_path)):
        all_files = []
        for file_name in os.listdir(abs_path):
            all_files.append(abs_path + '/' + file_name)
        return all_files

def find_password(list_of_files = cached_files()):
    for item in list_of_files:
        with open(item, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if (line[0] != '0'):
                    password = line[line.find(' ')+1:line.find('\\')]
                    return password

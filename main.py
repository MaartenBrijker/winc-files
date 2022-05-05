__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile

PATH = os.path.join(os.getcwd(), 'cache')

def clean_cache():
    if os.path.exists(PATH):
        for file_name in os.listdir(PATH):
            file = os.path.join(PATH, file_name)
            if os.path.isfile(file):
                os.remove(file)  
    else: 
        os.mkdir(PATH) 
             
def cache_zip(zip_path, cache_path):
    clean_cache()
    with ZipFile(zip_path, 'r') as zipObj:
        zipObj.extractall(path=cache_path)

def cached_files():
    if (os.path.exists(PATH)):
        all_files = []
        for file_name in os.listdir(PATH):
            all_files.append(PATH + '/' + file_name)
        return all_files

def find_password(list_of_files = cached_files()):
    for item in list_of_files:
        with open(item, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if (line[0] != '0'):
                    password = line[line.find(' ')+1:line.find('\\')]
                    return password

# clean_cache()
# cache_zip('data.zip', PATH)
# print(find_password(cached_files()))
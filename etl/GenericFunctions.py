#!/usr/bin/env python
# Luis Enrique Fuentes Plata

from __future__ import annotations
from typing import Optional

def getDaysSince(_date:str='2018-01-01')->int:
    """Returns the number of days since a specific date in the form o YYY-MM-DD
    
    Arguments:
        _date (str): 2018-01-01
    Returns: 
        (int)
    """
    import datetime as dt
    return (dt.datetime.now().date() - dt.datetime.strptime(_date,'%Y-%m-%d').date()).days

def decoratorGetToken(function):
    def wrapper():
        from os import environ
        return environ.get('TOKEN')
    return wrapper
@decoratorGetToken
def getToken()->str:
    """Returns the Token privided by TSheets this is needed to execute locally when deployed the decorator
       needs to be activated. 
    
    Arguments:
        None
    Returns: 
        (str)
    """
    return '' # Add the token here for local testing

def decoratorGetPath(function):
    def wrapper(file_name:str):
        from pathlib import Path
        return Path('/tmp', file_name)
    return wrapper
@decoratorGetPath
def getPath(file_name:str):
    """For local testing this method returns the working directory
    
    Arguments:
        file_name (str) : myfile.csv
    Returns: 
        (Path)
    """
    from os import getcwd
    from pathlib import Path
    return Path(getcwd(), file_name)

def send_to_bucket(file_full_path:str)->None:
    """Uploads an object/file to a GCP bucket Example: app-script-data-extraction-output/tsheets/myfile.csv

    Arguments:
        file_full_path (str): String for the the file full path
    Returns: 
        None
    """
    from google.cloud import storage
    from os.path import basename

    file_name = basename(file_full_path) 

    dictionary = {'bucketName': 'app-script-data-extraction-output',
                  'destination_blob_name': f'tsheets/{file_name}',
                  'source_file_name': f'{file_full_path}'}
    storage_client = storage.Client()
    storage_client.get_bucket(dictionary['bucketName']).blob(dictionary['destination_blob_name'])\
        .upload_from_filename(dictionary['source_file_name'])


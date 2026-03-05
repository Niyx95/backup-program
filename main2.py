#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
import shutil, logging

#check if given source path is valid
def check_source():
    #ask user to set path to backup
    source = input('Please set path to back-up: > ').strip()
    source_dir = Path(source)
    #loop until user set a valid path
    while not source_dir.exists():
        choice = input('Please enter a valid path > ').strip()
        source_dir = Path(choice)
    #return Path object to capture data
    return source_dir

#check if the given destination path is valid
def check_destination():
    # #ask user to set destination path
    destination = input('Please set path to destination: > ').strip()
    destination_dir = Path(destination)
    #loop until user set a valid path
    while not destination_dir.exists():
        choice =  input('Please enter a valid destination path. > ').strip()
        destination_dir = Path(choice)
    #return Path object to capture data
    return destination_dir

#copy and compress chosen dir for backup
def copy_and_compress(source, destination):
    try:
    #set time and date and create tar file
        date = datetime.now()
        name = destination / f'Your back-up has been created on: {date}'

        archive = shutil.make_archive(base_name=str(name),
                                      format='gztar',
                                      root_dir=str(source.parent),
                                      base_dir=source.name)
        return archive

    except Exception as error:
        print(f'sorry, an {error} accured')

#function to save the backup to google cloud service
def cloud():
    creds = 'BackupClient.json'





copy_and_compress(source=check_source(), destination=check_destination())
















#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
import shutil

#config:
SOURCE_DIR = Path.home() / 'Documents' / 'MyDir'
DESTINATION_DIR = Path.home() / 'backups' / 'test_backups'
# KEEP_LOCAL = True

date = datetime.now().strftime('%Y-%m-%d-%H-%M')
name = f'{SOURCE_DIR.name}_{date}'
destination = DESTINATION_DIR / name

#check path availability
def check_path():
    try:
        #check if dir path exists
        if not SOURCE_DIR.exists():
            print(f'{SOURCE_DIR} has not been found!')

        #create a new directory if it doesn't exist
        if not DESTINATION_DIR.exists():
            destination.mkdir(parents=True, exist_ok=True)

    except Exception as error:
        print(error)

#create and compress .tar file / create logs
def compress():
    try:
        #create tar file
        create = shutil.make_archive(base_name=str(destination),
                                     format='gztar',
                                     root_dir=SOURCE_DIR)
        #create a text file to log backup information
        logs = DESTINATION_DIR / 'logs.txt'
        with open(logs, 'a') as logs:
            logs.write(f'Backup created on {date} in path {DESTINATION_DIR}\n')
        #create a text file if error is detected
    except Exception as error:
        logs = DESTINATION_DIR / 'logs.txt'
        with open(logs, 'a') as logs:
            logs.write(f'{date} Backup failed: {error}\n')

check_path()
compress()
#!/usr/bin/env python3

import shutil, os.path
from pathlib import Path
from datetime import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

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

    #set time and date and create tar file
    date = datetime.now()
    name = destination / f'Your back-up has been created on: {date}'

    archive = shutil.make_archive(base_name=str(name),
                                      format='gztar',
                                      root_dir=str(source.parent),
                                      base_dir=source.name)
    return archive

    

#function to save the backup to Google Cloud service
def cloud(backup):
    scopes = ["https://www.googleapis.com/auth/documents"]  #define permissions needed
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", scopes)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "BackupClient.json", scopes
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("docs", "v1", credentials=creds)

         # Retrieve the documents contents from the Docs service.
        DOCUMENT_ID = input('please enter you document id: > ').strip()
        print(f"Document created with id {DOCUMENT_ID}")
        #make request
        requests = [
              {
                'insertText': {
                    'location': {
                        'index': 1,
                     },
                      'text': f'backup created in date {datetime.now()}\nFile: {backup}\n'
                }
             }
           ]

        #exeute the batch update
        result = service.documents().batchUpdate(
               documentId=DOCUMENT_ID, body={'requests': requests}).execute()
        #print
        print('uploaded successfully')

    except HttpError as err:
         print(err)


archive = copy_and_compress(source=check_source(), destination=check_destination())

cloud_choice = input('Do you want to save the backup to your google cloud? (y/n) > ').strip().lower()
if cloud_choice == 'y':
    cloud(archive)

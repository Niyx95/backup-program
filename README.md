AUTHOR:
nyx.2k

NAME:
Backup Program

Hello everyone, I`m Nyx. This is my first real project. A small Backup program for your files. 

The idea came into my mind when I was on the Great Barrier Reef in Australia and heading back home looking at my GoPro thinking I need a backup of this beautiful experience, and slowly it became real. 
I am very proud of my code. It`s not perfect but it`s mine. I am a rookie coder and I hope you can appreciate it and maybe use it for yourself.

USAGE:
The program will ask the user to set a source directory and a destination directory.
After that it will compress the source into a .tar.gz file and store it where prompted.
The program will ask also if the user wants to save logs into google docs document.
(keep in mind you need to provide a DOCUMENT ID to save it to an existing Doc.)

EXECUTION:
open the terminal and run the program (./main.py)
follow the prompts. Maybe you need to change the shebang on line 1 in main.py, to path of your python directory. 

REQUIREMENTS:
- Python 3.14+
- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib
- A Google Cloud project with Docs API enabled
- A Google Docs API credentials file (BackupClient.json)

FUTURE UPDATES:
-Google Drive integration to save your file directly to the cloud.

~~THANKS FOR READING~~

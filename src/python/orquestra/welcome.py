"""
This module saves a welcome message.
"""

import json
import time
import os
import pwd
import subprocess
import requests

def welcome():
    message = "Hello World from Orquestra!"
    print("Args:", ref_artifact_1, ref_artifact_2)
    message_dict = {}
    message_dict["message"] = message
    message_dict["schema"] = "message"

    with open("welcome.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact
        print(os.environ)
        print("USER:" + pwd.getpwuid( os.getuid() )[ 0 ])
        subprocess.call(['pwd'])
        time.sleep(3600)
    for i in range(10):
        resp = requests.get("https://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json")
        print(f"HTTP: {resp}")
        for j in range(5):
            time.sleep(300)
            response = requests.get("https://api.spacexdata.com/v4/launches/latest")
            print(f"HTTPS: {response}")
            
            
    print('''
|-----------------------------------------------------------------------|
|    o   \ o /  _ o         __|    \ /     |__        o _  \ o /   o    |
|   /|\    |     /\   ___\o   \o    |    o/    o/__   /\     |    /|\   |
|   / \   / \   | \  /)  |    ( \  /o\  / )    |  (\  / |   / \   / \   |
|-----------------------------------------------------------------------|
        ''')
        

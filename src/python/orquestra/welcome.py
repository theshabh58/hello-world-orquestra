"""
This module saves a welcome message.
"""

import json
import time
import os
import pwd

def welcome():
    message = "Hello World from Orquestra!"

    message_dict = {}
    message_dict["message"] = message
    message_dict["schema"] = "message"

    with open("welcome.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact
        print(os.environ)
        print("USER:" + pwd.getpwuid( os.getuid() )[ 0 ])
        time.sleep(3600)

"""
This module saves a welcome message.
"""

import json
import time

def welcome():
    message = "Hello World from Orquestra!"

    message_dict = {}
    message_dict["message"] = message
    message_dict["schema"] = "message"

    with open("welcome.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact
        time.sleep(3600)
"""
This module saves a welcome message
"""

import json

def welcomeMsg():
    message = "Hello World from Orquestra!"
    
    message_dict = {}
    message_dict["message"] = message
    message_dict["schema"] = "message"

    with open("welcome.json", 'w') as f:
        #open and write a message to file that will serve as an artifcat.
        f.write(json.dump(message_dict, indent=2))
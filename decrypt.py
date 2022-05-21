import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "rans.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
    
print(files)
# print(key)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

for file in files:
    with open(file, "rb") as thefile:
        content = thefile.read()
    content_decrypted = Fernet(secretkey).decrypt(content)
    with open(file, "wb") as thefile:
        thefile.write(content_decrypted)
        
print('Your files are decrypted!')
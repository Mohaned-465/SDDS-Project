import os
from encrypt import encrypt_file

def self_destruct(file):

    if os.path.exists(file):

        choice = input("1 Delete / 2 Encrypt: ")

        if choice == "1":
            os.remove(file)
            print("File deleted")

        elif choice == "2":
            encrypt_file(file)

        else:
            print("No action")

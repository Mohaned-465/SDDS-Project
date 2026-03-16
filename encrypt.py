from cryptography.fernet import Fernet

def encrypt_file(file):

    key = Fernet.generate_key()
    cipher = Fernet(key)

    with open(file, "rb") as f:
        data = f.read()

    encrypted = cipher.encrypt(data)

    with open(file, "wb") as f:
        f.write(encrypted)

    print("File encrypted")

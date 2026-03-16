from security import self_destruct

file = "data.txt"

with open("password.txt") as f:
    real_password = f.read().strip()

password = input("Enter password: ")

if password == real_password:
    print("Access granted")
else:
    print("Wrong password")
    self_destruct(file)

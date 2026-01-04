import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

users = {}

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    users[username] = hash_password(password)
    print("User registered successfully.")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed = hash_password(password)

    if username in users and users[username] == hashed:
        print("Login successful.")
    else:
        print("Invalid username or password.")

while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid option.")

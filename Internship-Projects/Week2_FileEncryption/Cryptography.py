from cryptography.fernet import Fernet
import os

# Generate encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as secret.key")


# Load existing key
def load_key():
    return open("secret.key", "rb").read()


# Encrypt file
def encrypt_file(filename):
    try:
        key = load_key()
        fernet = Fernet(key)

        with open(filename, "rb") as file:
            data = file.read()

        encrypted = fernet.encrypt(data)

        with open(filename, "wb") as file:
            file.write(encrypted)

        print("File encrypted successfully!")

    except FileNotFoundError:
        print("File not found!")


# Decrypt file
def decrypt_file(filename):
    try:
        key = load_key()
        fernet = Fernet(key)

        with open(filename, "rb") as file:
            encrypted_data = file.read()

        decrypted = fernet.decrypt(encrypted_data)

        with open(filename, "wb") as file:
            file.write(decrypted)

        print("File decrypted successfully!")

    except FileNotFoundError:
        print("File not found!")


# Menu system
while True:
    print("\n--- File Security Tool ---")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        generate_key()

    elif choice == '2':
        file_name = input("Enter file name to encrypt: ")
        encrypt_file(file_name)

    elif choice == '3':
        file_name = input("Enter file name to decrypt: ")
        decrypt_file(file_name)

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
import os
from tqdm import tqdm
from cryptography.fernet import Fernet

KEY_FILE = ".key"

def generate_key():
    key = Fernet.generate_key()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    key_path = os.path.join(script_dir, KEY_FILE)
    with open(key_path, "wb") as key_file:
        key_file.write(key)

def load_key():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    key_path = os.path.join(script_dir, KEY_FILE)
    with open(key_path, "rb") as key_file:
        key = key_file.read()
    return key

def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def get_files_to_process():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    files = []
    for file in os.listdir(script_dir):
        file_path = os.path.join(script_dir, file)
        if (
            file != KEY_FILE
            and file != os.path.basename(__file__)
            and not file.endswith(".key")
            and os.path.isfile(file_path)
        ):
            files.append(file_path)
    return files

def encrypt_files():
    key = load_key()
    files = get_files_to_process()
    with tqdm(total=len(files), desc="Encrypting files") as pbar:
        for file_path in files:
            encrypt_file(file_path, key)
            pbar.set_postfix({"Current File": os.path.basename(file_path)})
            pbar.update(1)

def decrypt_files():
    key = load_key()
    files = get_files_to_process()
    with tqdm(total=len(files), desc="Decrypting files") as pbar:
        for file_path in files:
            decrypt_file(file_path, key)
            pbar.set_postfix({"Current File": os.path.basename(file_path)})
            pbar.update(1)

if __name__ == "__main__":
    action = input("Enter 'encrypt' or 'decrypt': ")

    if action == "encrypt":
        script_dir = os.path.dirname(os.path.abspath(__file__))
        key_path = os.path.join(script_dir, KEY_FILE)
        if not os.path.exists(key_path):
            generate_key()
        encrypt_files()
        print("Files encrypted successfully.")
    elif action == "decrypt":
        script_dir = os.path.dirname(os.path.abspath(__file__))
        key_path = os.path.join(script_dir, KEY_FILE)
        if not os.path.exists(key_path):
            print("No key file found. Please place the key file in the current directory.")
        else:
            decrypt_files()
            print("Files decrypted successfully.")
    else:
        print("Invalid action. Please enter 'encrypt' or 'decrypt'.")

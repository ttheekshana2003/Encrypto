
# Encrypto

Encrypto is a Python-based file encryption and decryption tool. It provides a simple and secure way to encrypt and decrypt files within a directory, ensuring the confidentiality of your sensitive data.

## Features

- Encrypts files within the specified directory
- Decrypts encrypted files using the encryption key- 
- Provides a progress bar to track the encryption/decryption process
- Uses the Fernet encryption algorithm from the cryptography library

## Getting Started


### Usage

1. Place the files you want to encrypt/decrypt in the same directory as the `Encrypto.exe`

2. Run the file.
This will encrypt all the files within the directory, except the key file and the `encrypto.py` script.

3. To decrypt files, make sure you have the key file (`key.key`) in the project directory, and then run the `Encrypto.exe` again. 


This will decrypt the previously encrypted files using the key file.

5. Follow the on-screen instructions and monitor the progress bar to track the encryption/decryption process.

## Security

- **Encrypto** uses the *Fernet encryption algorithm from the cryptography library*, which is a strong and secure encryption algorithm based on symmetric key cryptography.
- It generates a unique key file (`key.key`) that is required for both encryption and decryption. Make sure to keep this key file secure and do not share it with unauthorized individuals.
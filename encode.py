from PIL import Image
import numpy
from cryptography.fernet import Fernet

file_path = 'example_key.txt'

password = input("Input password: ")
image_path = input("Input image path: ")

try:
    with open (file_path, 'r') as file:
        key_str = file.read().strip()

        if key_str.startswith("b'") and key_str.endswith("'"):
            key = key_str[2:-1].encode()
        else:
            key = key_str.encode()
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

f = Fernet(key)
password_bytes = password.encode()

encrypted_token = f.encrypt(password_bytes)

print ("Password: ", password)
print ("Encrypted token: ", encrypted_token)
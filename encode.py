from cryptography.fernet import Fernet
from utils.bit_utils import add_delimiter
from utils.image_utils import encode_image

file_path = 'example_key.txt'

password = input("Input password: ")
image_path = input("Input image path: ")

try:
    open (image_path, 'r')
except FileNotFoundError:
    print(f"Error: The file '{image_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

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

token = add_delimiter(encrypted_token)

#print ("Password: ", password)
#print ("Encrypted token: ", encrypted_token)

encode_image(image_path, token)
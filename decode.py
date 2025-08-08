from utils.image_utils import decode_image
from utils.bit_utils import bits_to_bytes
from cryptography.fernet import Fernet

image_path = 'encoded_image.png'
file_path = 'example_key.txt'

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

try:
    open (image_path, 'r')
except FileNotFoundError:
    print(f"Error: The file '{image_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

bitstring = decode_image(image_path)

encrypted_bytes = bits_to_bytes(bitstring)

f = Fernet(key)
plaintext = f.decrypt(encrypted_bytes).decode()

print("Password:", plaintext)
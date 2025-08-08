from cryptography.fernet import Fernet

key = Fernet.generate_key()

key_file = "example_key.txt"
with open(key_file, "w") as file:
  file.write(str(key))
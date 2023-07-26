from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import configparser
import hashlib
import secrets

key_file = "aes_key.ini"

config = configparser.ConfigParser()
config.read(key_file)

# Retrieve the key from the .ini file
key = bytes.fromhex(config['Keys']['AESKey'])
block_size = 16  # AES block size is 16 bytes


def encrypt(data):
    # Use the key for encryption and decryption
    data = data.encode()
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(data, block_size)
    ciphertext = cipher.encrypt(padded_data)
    return ciphertext.hex()


def decrypt(ciphertext):
    print(type(ciphertext))
    decipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = decipher.decrypt(bytes.fromhex(ciphertext))
    unpadded_data = unpad(decrypted_data, block_size)
    unpadded_data_str = unpadded_data.decode()
    return unpadded_data_str


def password_hash(password):
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()

    # Hash the password
    hash_object.update(password.encode('utf-8'))

    # Get the hashed password as a hexadecimal string
    hashed_password = hash_object.hexdigest()

    return hashed_password


def salted_password(password):
    # Generate a random salt (16 bytes)
    salt = secrets.token_bytes(16)

    # Append the salt to the password
    salted_password = salt + password.encode('utf-8')

    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()

    # Hash the salted password
    hash_object.update(salted_password)

    # Get the hashed password as a hexadecimal string
    hashed_password = hash_object.hexdigest()

    return hashed_password, salt

    # Example usage:
    # user_password = "my_password"
    # hashed_password, salt = password_hash(user_password)

# print(ciphertext)
# print(unpadded_data)  # Output: b"Hello, World!"

from Crypto.Random import get_random_bytes

# Generate a random AES key
key = get_random_bytes(16)  # Generate a 16-byte (128-bit) random AES key

# Save the key to a file
key_file = "aes_key.ini"

hex_key = key.hex()

with open(key_file, "w") as f:
    f.write("[Keys]\n")
    f.write("AESKey = " + hex_key)

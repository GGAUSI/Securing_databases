import os
import subprocess
from cryptography.fernet import Fernet
import base64

# Replace these variables with your own settings
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'sakila'
BACKUP_DIR = 'backups/'
ENCRYPTED_BACKUP_DIR = 'backups/encrypted/'

# Generate the encryption key using Fernet
key = Fernet.generate_key()
SECRET_KEY = key
cipher_suite = Fernet(SECRET_KEY)

MYSQLDUMP_PATH = 'C:/xampp/mysql/bin/mysqldump.exe'

try:
    # Create a backup of the database using mysqldump
    backup_file = os.path.join(BACKUP_DIR, f'{DB_NAME}_backup.sql')
    backup_cmd = [MYSQLDUMP_PATH, '-u', DB_USER, f'--password={DB_PASSWORD}', DB_NAME]
    print("Running backup command:", " ".join(backup_cmd))
    with open(backup_file, 'wb') as file:
        subprocess.run(backup_cmd, stdout=file, check=True)

    print(f"Database backup created: {backup_file}")

    # Encrypt the backup file
    encrypted_backup_file = os.path.join(ENCRYPTED_BACKUP_DIR, f'{DB_NAME}_backup_encrypted')
    with open(backup_file, 'rb') as file:
        original_data = file.read()
    encrypted_data = cipher_suite.encrypt(original_data)

    with open(encrypted_backup_file, 'wb') as file:
        file.write(encrypted_data)

    print(f"Backup encrypted and saved as: {encrypted_backup_file}")

    # Optionally, you can delete the unencrypted backup file to enhance security
    os.remove(backup_file)
    print(f"Unencrypted backup file deleted: {backup_file}")

    # Display the generated key
    print("Generated encryption key:", base64.urlsafe_b64encode(key).decode())

except subprocess.CalledProcessError as e:
    print(f"Error: Unable to create database backup. Command returned non-zero exit status.")
    print(e)
except Exception as e:
    print(f"An unexpected error occurred: {e}")

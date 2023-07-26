from db_connection import connect, disconnect
import encrypt_decrypt

conn = connect()
cursor = conn.cursor()

import binascii
def is_hexadecimal(s):
    try:
        bytes.fromhex(s)
        return True
    except ValueError:
        return False





def encrypt():
    # Fetch data from the database
    select_query = "SELECT trans_id, Account_Number FROM financial_data"
    cursor.execute(select_query)
    rows = cursor.fetchall()

    # Encrypt and update the data
    for row in rows:
        account_id, acc = row
        # Assuming 'balance' is a numeric value that needs to be encrypted
        encrypted_acc = encrypt_decrypt.encrypt(acc)
        # Update the encrypted data in the database
        update_query = "UPDATE financial_data SET Account_Number = %s WHERE trans_id = %s"
        cursor.execute(update_query, (encrypted_acc, account_id))

    # Commit the changes to the database
    conn.commit()

    # Close the database connection


def decrypt_accounts(ecncryprio=None):
    select_query = "SELECT trans_id, Account_Number FROM financial_data"
    cursor.execute(select_query)
    rows = cursor.fetchall()

    # Decrypt and update the data
    for row in rows:
        account_id, acc = row
        decrypted_acc = encrypt_decrypt.decrypt(acc)  # Convert hex to bytes
        update_query = "UPDATE financial_data SET Account_Number = %s WHERE trans_id = %s"
        cursor.execute(update_query, (decrypted_acc, account_id))

    # Commit the changes to the database
    conn.commit()

    # Close the database connection
    #disconnect()




# encrypt()
# decrypt_accounts()
from tkinter import messagebox
import tkinter as tk
from db_connection import connect, disconnect
import encrypt_decrypt as encryption

# Connect to the database
conn = connect()
cursor = conn.cursor()


def create_account(data, labels):
    # Retrieve the entered account details
    fname = data[0]
    sname = data[1]
    gender = data[2]
    email = data[3]
    password = data[4]
    account_no = data[5]
    state = data[6]
    ssn = data[7]

    # Perform validation and create the account
    ssn = encryption.encrypt(ssn)
    account_no = encryption.encrypt(account_no)
    if validate_inputs(fname, sname, gender, state, email, password, account_no, ssn):
        # Create the account in the banking application
        hashed_password = encryption.password_hash(password)
        cursor.execute("SELECT COUNT(*) FROM customers WHERE email = %s", (email,))
        count = cursor.fetchone()[0]

        if count > 0:
            # Handle the duplicate email case, for example:
            print("Error: Email already exists.")
        else:
            sql = "INSERT INTO customers (first_name, last_name, gender, city, email, password, account_number, ssn) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (fname, sname, gender, state, email, hashed_password, account_no, ssn)
            cursor.execute(sql, values)
            conn.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "Account created successfully!")
                for i in labels:
                    i.delete(0, tk.END)
            else:
                print("No rows were inserted.")

        cursor.close()
        conn.close()
    else:
        messagebox.showerror("Error", "Invalid input. Please check the entered details.")



def validate_inputs(fname, email, password, address, sname, gender, account_no, ssn):
    # Perform validation on the entered inputs
    # Add more validation rules as per your requirements

    return all([fname, email, password, address, sname, gender, account_no, ssn])





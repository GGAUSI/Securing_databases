NECESSARY LIBRARIES
execute these commands in your terminal to have the necessary dependencies
pip3 install pillow
pip3 install mariadb
pip3 install cryptography
pip3 install pycryptodome


DATABASE
Create a new database named sakila and import the sql file found here
I am mainly dealing with the tables 'customers' and 'financial data'

PYTHON FILES
1. aes_key.ini
It contains the encryption key. I recommend you delete this file once you pull the code from the repository and then run the 'create_ini.py' file followed by the 'generate_key.py' file so it can generate the aes_ini file properly on your machine

2. backup_encryption
This file is meant to generate a backup file for the database, create an encrypted version of this file, and delete the normal backup file
NOTE: This line --> MYSQLDUMP_PATH = 'C:/xampp/mysql/bin/mysqldump.exe' may bring an error on your machine depending on the configuration of your database enviroment. if you are using wamp replace the path with the path where the 'mysqldump.exe' file is located on your computer

3. This file contains logic for adding a user into the 'Customers' table of our database. it encrypts the account number and ssn, and it hashes the passsword

4. db_connection
This file connects to the database. I have connected to the database once in this file, and I import this connection in all the other files where I need to connect to the database.

5. column_encryption
This file does the column level encryption and decryption. at the end there are 2 function calls as follows:
# encrypt()
# decrypt_accounts()
To encrypt, uncomment(By removing the hashtag) the encrypt function and to decrypt uncomment the decrypt_column one
it encrypts the field 'Account_Number' in the financial_data table of the database

6. encrypt_decrypt
This is where the actual encryption, decryption, and hashing is done. it has 3 functions that perform these three operations. 

7. main
It takes you to a login page where you can either login or sign up if you dont have an account. If you are going to sign up use a valid email address. it will take the details you enter and hash the password, and then encrypt the acciunt number and ssn and send it to the database. once you sign up, terminate the program and run the main again to login because I haven't incorporated navigation controls

once you put the right credentials at login, it will send you a one time password to your email, and take you to a page where you can enter that code to sucessfully login. then you have a welcome page

8. OTP_verification
it contains the logic for one time password functionality

OTHER FOLDERS
The backup folder is for the database backup encryption. once you run the function, the encrypted file is saved in the encrypted directory inside the backup folder

the images folder is holding the images# Securing_databases

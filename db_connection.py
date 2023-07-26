import mariadb
import sys
from mariadb import Error


def connect():
    try:
        conn = mariadb.connect(
            user="root",
            password="",
            host="127.0.0.1",
            port=3306,
            database="sakila"

        )
        return conn
    except Error as e:
        print(f"Error connecting to MariaDB: {e}")
        return None


def disconnect(conn):
    if conn.is_connected():
        conn.close()
        print("Connection to MariaDB closed.")

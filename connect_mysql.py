import mysql.connector
from mysql.connector import Error

def connect_database():
    # connecting to OUR databse - e_commerce_db
    db_name = "e_commerce_db"
    user = "root"
    password = "Buttmuffin3!"
    host = "localhost" #127.0.0.1

    try:
        # attempting to establish a connection
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )

        # checking if the connection is succesful
        if conn.is_connected(): #returns True if a connection was successfully made
            return conn
            

        # handling any connection errors
    except Error as e:
        print(f"Error: {e}")

    






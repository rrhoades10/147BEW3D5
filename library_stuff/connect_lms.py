import mysql.connector
from mysql.connector import Error
from pw import password

def connect_db():
    # connecting to OUR databse - e_commerce_db
    db_name = "library_management_system"
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
            print("(*￣3￣)╭")
            return conn
            

        # handling any connection errors
    except Error as e:
        print(f"Error: {e}")

connect_db()

    






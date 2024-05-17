from connect_mysql import connect_database
from mysql.connector import Error

def fetch_orders():
    try:
        conn = connect_database()
        cursor = conn.cursor()

        query = "SELECT * FROM Orders"

        cursor.execute(query)

        # loop through all rows returned from ORders
        for row in cursor.fetchall():
            print(row)     
        

    except Error as e:
        print(f"Error as {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

fetch_orders()
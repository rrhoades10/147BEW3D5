from connect_mysql import connect_database
from mysql.connector import Error

def update_order(): #update customers phone
    try:
        conn = connect_database()
        cursor = conn.cursor()

        o_id = input("What is the id of the order youd like to update? ")
        order_date = input("What is the corrected order date? ")

        updated_order = (order_date, o_id)
        # Update query
        query = "UPDATE Orders SET date = %s WHERE order_id = %s"

        # executing the query
        cursor.execute(query, updated_order)
        conn.commit()
        print("Order succesfully updated!")

       

    except Error as e:
        print(f"Error as {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

update_order()
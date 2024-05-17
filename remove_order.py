from connect_mysql import connect_database
from mysql.connector import Error

def remove_order():
    try:
        conn = connect_database()
        cursor = conn.cursor()


        o_id = input("Please enter the id of the order you'd like to remove: ")

        removed_order = (o_id,)

        # DELETE Query
        query = "DELETE FROM Orders WHERE order_id = %s" 

        cursor.execute(query, removed_order)
        conn.commit()
        print("Order was successfully deleted!")       

       

    except Error as e:
        print(f"Error as {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

remove_order()

from connect_mysql import connect_database
from mysql.connector import Error

def add_order():
    try:
        conn = connect_database()
        cursor = conn.cursor()
        
        # taking an input for the customer_id to add an order to
        c_id = input("What is the id of the customer you'd like to add an order to? ")
        order_date = input("When was this order made? ")

        order = (order_date, c_id)

        # SQL Query to Insert
        query = "INSERT INTO Orders (date, customer_id) VALUES (%s, %s)"

        # executing the query
        cursor.execute(query, order)
        conn.commit()
        print("Order successfully added!")          
        

    except Error as e:
        print(f"Error as {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

add_order()
from connect_mysql import connect_database
from mysql.connector import Error

def update_customer(): #update customers phone
    try:
        conn = connect_database()
        cursor = conn.cursor()

        # setting tuple with information to update
        phone = input("What is the updated phone number? ")
        c_id = input("Which customer id would you like to update?")

        updated_customer =(phone, c_id)
        # SQL query to update customer phone where id = 10

        query = "UPDATE Customers SET phone = %s WHERE customer_id = %s"
        cursor.execute(query, updated_customer) 
        conn.commit()
        print("Customer succesfully updated!")    

       

    except Error as e:
        print(f"Error as {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

update_customer()
from connect_mysql import connect_database
from mysql.connector import Error

def remove_customer():
    try:
        conn = connect_database()
        cursor = conn.cursor()

        # creating a tuple with a single item for the customer id
        c_id = input("Which customer would you like to remove by id?")
       
        removed_customer = (c_id,)
        # query our Orders to see if the customer_id shows up as a foreign key
        query_check = "SELECT * FROM Orders where customer_id = %s"
        cursor.execute(query_check, removed_customer)
        orders = cursor.fetchall()
        # if it is True that we've received a collection of orders
        if orders:
            # then we do nothing because of the below reason
            print("Cannot delete customer: Customer has associated orders.")
        # if no orders are found, we can delete that customer
        else:

            # SQL Query
            query = "DELETE FROM Customers WHERE customer_id = %s"

            # executing the query
            cursor.execute(query, removed_customer)
            conn.commit()
            print("Customer was removed succesfully!")

       

    except Error as e:
        print(f"Error as {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

remove_customer()

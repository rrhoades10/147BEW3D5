from connect_mysql import connect_database
from mysql.connector import Error
from fetch_customers import fetch_customers

def add_customer():
    try:
        conn = connect_database()
        cursor = conn.cursor()

        # Creating information for a new customer
        #                 name                 email                phone
        new_customer = ("Ryan Rhoades", "ryanr@codingtemple.com", "6308247768")
        # the above ALWAYS needs to be an iterable (preferably a tuple) so we can apply the items positionally to the 
        # values in our insert statement, which are inserted into their respective columns

        # Insert Query                                             name  email phone
        query = "INSERT INTO Customers(name, email, phone) VALUES (%s, %s, %s)"
        cursor.execute(query, new_customer) #executes the insert statement and applies the items from the new_customer variable
        conn.commit() #commits my changes
        print("New customer added succesfully")
        fetch_customers()

    except Error as e:
        print(f"Error as {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

add_customer()



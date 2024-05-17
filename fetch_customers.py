from connect_mysql import connect_database


def fetch_customers():
    conn = connect_database()

    if conn:
        try:
            cursor = conn.cursor() #cursor allows us to execute SQL queries within python

            # SQL Query to fetch all customers
            # storying the query in a python string
            query = "SELECT * FROM Customers"

            # executing the query
            cursor.execute(query)

            # loop through query data with cursor.fetchall()
            # fetchall() returns all the information from the query
            for row in cursor.fetchall():
                print(row)
        
        finally:
            cursor.close()
            conn.close()
# use this for testing, so when you eventually import, you dont accidentally call this function
if __name__ == "__main__":
    fetch_customers()



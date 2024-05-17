import mysql.connector

# for any database we're connecting you
# using mysql.connector to connect to our db
db_name = "your_dbname"
user = "db_user"
password = "dbpassword"
host = "your_host likely going to be localhost"

# create the connection with the above variables
conn = mysql.connector.connect(
    database=db_name,
    user=user,
    password=password,
    host=host
)




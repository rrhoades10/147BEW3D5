from connect_lms import connect_db
from mysql.connector import Error
# class Libary:
#     def __init__(self):
#         self.authors = [] 
#     def add_author(self):
#         try:
#             conn = connect_db()
#             cursor = conn.cursor


#             author = input("Who is the author? ")
#             biography = input("Enter some info about the author: ")
#             author = Author(author, biography)
#             self.authors.append(author)

#             query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
#             cursor.execute(query, (author.name, author.biography)) # or you can set the second argument to a tuple
#             conn.commit()


# class Author:
#     def __init__(self, name, biography):
#         self.name = name
#         self.biography = biography

#     def add_to_db(self):
#         try:
#             conn = connect_db()
#             cursor = conn.cursor
            

#             query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
#             cursor.execute(query, (self.name, self.biography)) # or you can set the second argument to a tuple
#             conn.commit()

# author = Author("Tolkien", "He wrote lord of the rings it was dope")
# author.add_to_db()

def add_author():
        try:
            conn = connect_db()
            cursor = conn.cursor()


            author = input("Who is the author? ")
            biography = input("Enter some info about the author: ")            
            

            query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
            cursor.execute(query, (author, biography)) # or you can set the second argument to a tuple
            conn.commit()
            print('Succesfully added author!')

        except Error as e:
              print(f"Error: {e}")

        finally:
              if conn and conn.is_connected():
                    cursor.close()
                    conn.close()

add_author()
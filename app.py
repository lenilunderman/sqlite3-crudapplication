import sqlite3

#create the connection to the database
conn = sqlite3.connect('database')
#create the cursor to execute the queries
cursor = conn.cursor()

#create a table
cursor.execute('''
                CREATE TABLE USERS(id INTEGER PRIMARY KEY, name TEXT, 
                phone TEXT, email TEXT UNIQUE, password TEXT)'''
              )

#commit the changes
conn.commit()
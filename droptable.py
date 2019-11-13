import sqlite3

conn = sqlite3.connect('database')
cursor = conn.cursor()

#delete the table from the database
cursor.execute("DROP TABLE USERS")

#commit the changes
conn.commit()
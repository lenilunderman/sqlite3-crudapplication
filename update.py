import sqlite3

#connect to the database and create the cursor for queries
conn = sqlite3.connect('database')
cursor = conn.cursor()

#update de information inside the database
user_id = 1
phone = 2023029323

cursor.execute('''UPDATE USERS set phone=? where id=?''',(phone,user_id))

conn.commit()
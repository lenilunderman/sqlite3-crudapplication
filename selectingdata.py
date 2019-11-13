import sqlite3
# Retrieving Data (SELECT) with SQLite 

# open the connection to the database
conn = sqlite3.connect('database')
cursor = conn.cursor()

# selecting the data

#selecting the data
cursor.execute("SELECT name,email, phone from USERS")
#fetch only one user of the database
#user1 = cursor.fetchone()
#print(user1[0])

for row in cursor:
    print(f"\n Name: {row[0]}, Email:{row[1]}, Phone: {row[2]}")

# To retrive data with conditions, use again the "?" placeholder
user_id = 3
cursor.execute('''SELECT name, email, phone FROM users WHERE id=?''', (user_id,))
user = cursor.fetchone()
print(user)
  


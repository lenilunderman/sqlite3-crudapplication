import sqlite3

conn = sqlite3.connect('database')
cursor = conn.cursor()

user_id = 3

cursor.execute('''DELETE FROM USERS WHERE id=?''',(user_id,))

conn.commit()

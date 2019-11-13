import sqlite3
#connect to the database
conn = sqlite3.connect('database')
cursor = conn.cursor()

#get the data to be inserted inside the database
print("Insert information inside the database USERS: \n")

name =      input("Enter your name: ")
phone =     input("Enter your phone number: ")
email =     input("Enter your email: ")
password =  input("Enter your password: ")

# insert the data inside the database
cursor.execute('''INSERT INTO USERS (name,phone,email,password)
            VALUES (?,?,?,?)''',(name,phone,email,password))

print("Your information was sucessefully added to the database")

##### Adding many users ... 
#Insert several users use executemany and a list with the tuples:
#users = [(name1,phone1, email1, password1),
#         (name2,phone2, email2, password2),
#         (name3,phone3, email3, password3)]
#cursor.executemany(''' INSERT INTO users(name, phone, email, password) VALUES(?,?,?,?)''', users)

conn.commit()
conn.close()
import sqlite3
conn=sqlite3.connect("username.db")
cursor=conn.cursor()

cursor.execute('''
         CREATE TABLE  IF NOT EXISTS users(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         uername VARCHAR(20) UNIQUE,
         password TEXT
         )
         ''')


cursor.execute('''
       CREATE TABLE IF NOT EXISTS Registration(
       id INTEGER  PRIMARY KEY AUTOINCREMENT,
       user_id INTEGER,
       name VARCHAR(20),
       des TEXT,
       FOREIGN KEY(user_id) References users(id))
    ''')

# cursor.execute('''
#            CREATE TABLE IF NOT EXISTS Registration(
#            Id INTEGER AUTOINCREMENT,
#            User_Id INTEGER,
#            Name VARCHAR(20),
#            Des TEXT,
#            FOREIGN KEY(User_Id) REFERENCES users(Id)
#            )
#            ''')




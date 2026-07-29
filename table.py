import sqlite3
conn=sqlite3.connect("book.db")
cursor=conn.cursor()

cursor.execute('''
           CREATE  TABLE IF NOT EXISTS book(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name VARCHAR(20) UNIQUE,
           des VARCHAR(20)
              )
           ''')

cursor.execute('''
           CREATE TABLE IF NOT EXISTS author(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           aut_id INTEGER,
           aut_name VARCHAR(20),
           FOREIGN KEY(aut_id) REFERENCES  book(id))
            ''')
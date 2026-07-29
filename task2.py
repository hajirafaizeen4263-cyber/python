#employee 
import sqlite3
conn=sqlite3.connect("demo2.db")
cursor=conn.cursor()


cursor.execute('''
               CREATE TABLE  IF NOT EXISTS Employee(
               Id INTEGER PRIMARY KEY AUTOINCREMENT,
               Name VARCHAR(20),
               Department VARCHAR(20))
               ''')
conn.close()

def addemployees():
    conn=sqlite3.connect("demo2.db")
    cursor=conn.cursor()
    name=input("enter employee name: ")
    department=input("enter the employee department: ")
    cursor.execute(''' 
                   INSERT INTO Employee(name,department)
                   VALUES(?,?)
                   ''',(name,department))
    conn.commit()
    conn.close()

def viewemployees():
    conn=sqlite3.connect("demo2.db")
    cursor=conn.cursor()

    cursor.execute('''
                   SELECT * FROM Employee
                   ''')
    employees=cursor.fetchall()
    print("EMPLOYEES FOUND")
    print("_______________")
    for i in employees:
        print(f"employees {i[0]}-{i[1]}")
        

def searchemployees():
    conn=sqlite3.connect("demo2.db")
    cursor=conn.cursor()
    employee_name=input("enter the employee name: ")
    cursor.execute('''
                 SELECT * FROM Employee WHERE name=?
                   ''',(employee_name,))
    employees=cursor.fetchone()
    print("employee found")

def main():
    print("welcome to the employee table")
    ch=int(input("enter your choice 1. add \n 2. view \n 3. search \n 4. exit \n"))
    if ch==1:
        addemployees()
    elif ch==2:
        viewemployees()
    elif ch==3:
        searchemployees()
    else:
        print("invalid choice")
        
main()
    


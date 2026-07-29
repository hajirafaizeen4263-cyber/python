#database
import sqlite3
conn=sqlite3.connect("test.db")#establishing a conection with db
cursor=conn.cursor()#to interact with the database


#operations
# cursor.execute(
# '''
# CREATE TABLE Student(
#    name VARCHAR(20),
#    age INTEGER,
#    address TEXT
#    )
# '''

# )

# def addstudent():
#     conn=sqlite3.connect("first.db")
#     cursor=conn.cursor()
#     student_name=input("ennter the name of student: ")
#     student_age=int(input("enter the age of student: "))
#     student_address=input("enter the address of student: ")
#     cursor.execute ('''
#         INSERT INTO Student(name,age,address)
#                 VALUES(?,?,?)
                    
                    
#         ''',(student_name,student_age,student_address))
#     conn.commit()
#     print("student added")


# conn.close()

# def main():
#     while True:
#         print("welcome to student record")
#         ch=int(input("enter your choice 1.ADD\n 2.VIEW : "))
#         if ch==1:
#             addstudent()
#         else:
#             print("invalid choice")
#             break
# main()


cursor.execute('''
            CREATE  TABLE  IF NOT EXISTS Tasks(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR(20),
               des TEXT )
            ''')
conn.close()

def addtasks():
    conn=sqlite3.connect("test.db")
    cursor=conn.cursor()
    name=input("enter the task name: ")
    des=input("eter the description: ")
    cursor.execute(''' 
                   INSERT INTO Tasks(name,des)
                   VALUES(?,?)
                   
                   ''',(name,des))
    conn.commit()
    conn.close()

def viewtasks():
    conn=sqlite3.connect("test.db")
    cursor=conn.cursor()
    cursor.execute('''
                   SELECT * FROM Tasks
                  ''')
    tasks=cursor.fetchall()
    print("Tasks Found")
    print("____________")
    for i in tasks:
        print(f"tasks {i[0]}-{i[1]}")
    conn.commit()
    conn.close()

def searchtasks():
    conn=sqlite3.connect("test.db")
    cursor=conn.cursor()
    task_id=int(input("enter the task id: "))
    
    cursor.execute('''
                   SELECT * FROM Tasks WHERE id = ?
                   ''',( task_id,))
    conn.commit()
    print("found task")
    
def updatetasks():
    conn=sqlite3.connect("test.db")
    cursor=conn.cursor()
    td=int(input("enter the id: "))
    tname=input("enter the task name: ")
    tdes=input("enter the task description: ")
    cursor.execute('''
               UPDATE Tasks SET name=?,des=? WHERE id=?
               ''',(tname,tdes,td))
    conn.commit()
    print("updated")

def delete_tasks():
    conn=sqlite3.connect("test.db")
    cursor=conn.cursor()
    task_id=int(input("enter the id of task: "))
    ch=input("are you sure that you want to delete the task Y/N \n: ").lower()
    if ch=="Y":
        cursor.execute('''
                DELETE Tasks WHERE id=?)
                ''',(task_id,))
        conn.commit()
        print("task deleted")
    else:
        print("task not deleted")





def main():
    while True:
        print("welcome to the tasks to complete")
        ch=int(input("enter your choice 1.add \n 2.view \n 3.search \n 4.update \n 5.delete \n 6.exit \n : "))
        if ch==1:
            addtasks()
        elif ch==2:
            viewtasks()
        elif ch==3:
            searchtasks()
        elif ch==4:
            updatetasks()
        elif ch==5:
            delete_tasks()
        else:
            print("invalid choice")
main()


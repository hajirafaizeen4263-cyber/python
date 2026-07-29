#database
import sqlite3
conn=sqlite3.connect("first.db")#establishing a conection with db
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



#decorators-functions that enhances other function
#*args -arguments
# **kwargs-keyword arguments



# def saymyname(fun):
#     def wrapper():
#         print("say my name")
#         fun()
#         print("you are right")
#     return wrapper
# @saymyname
# def add():
#     print("add 2 numbers")
# add()



# def fullname(*args,**kwargs):
# print(kwargs)


# def fullname(**kwargs):
#     fullname(fname="robert",mname="drownie",lname="jr")
# fullname()




import time
# start=time.time()
# for i in range(1,6):
#     print(i)
#     time.sleep(1)
# stop=time.time()
# print("total time=",stop-start)



def totaltime(n):
    def inner(fun):
       def wrappers(*args,**kwargs):
         print("exeuted",n,"times")
         start=time.time()
         fun(*args,**kwargs)
         stop=time.time()
         print("total time:{stop-start}")
       return wrappers
    return inner
@totaltime(10)
def myname(n):
    for i in range(n):
        print(i)
        time.sleep(1)
myname(5)

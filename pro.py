# from  multiprocessing import Process
# import os

# x=5
# def work():
#     global x
#     x =x * 5
#     print("am working",x)
#     print(os.getpid())

# p1 = Process(target=work)
# p2 = Process(target=work)

# if __name__=="__main__":
#     print(x,"main process")
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()



#list  comprehension
# a=[i for i in range(1,101) if i%2==0]
# print(a)

#creata a list numbers that are multiple of 3 and 5
list=[i for i in range(1,100)   if i%3==0 and i%5==0]
print(list)
#create a list of firt 1000 numbers that has digit 6 in them
num=[i for i in range(1,1001) if "6" in str(i)]
print(num)


#age calculator
def age():
   age=lambda x,y: x-y
   x=int(input("enter the year you born:"))
   y=int(input("enter the current year:"))
   print(" your age:",y-x)
    
age()
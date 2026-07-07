#pattern h
# for i in range(1,6):
#     for j in range(1,6):
#         if j==1 or j==5 or i==3 :
#            print("*",end=" ")
#         else:
#            print(" ",end=" ")
#     print()
                 
#pattern i
# for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or i==5 or j==3:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
        
#pattern square
# for i in range (1,6):
#     for j in range(1,6):
#         if i==1 or i==5 or j==1 or j==5:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
    
# #pattern s
# for i in range(1,6):
#     for j in range(1,6):
#         if j==1 and i==2 or j==5 and i==4 or i==5 or i==3 or i==1  :
#             print("*",end="")
#         else:
#             print(" ",end="")
        
#     print()

#pattern s
for i in range(1,6):
    for j in range(1,6):
        if j==1 and i==2 or j==5 and i==4 or j==2 and i==1 or j==3 and i==1 or j==4 and i==1 or j==5 and i==1 or j==2 and i==3 or j==3 and i==3 or j==4 and i==3 or j==1 and i==5 or j==2 and i==5 or j==3 and i==5 or j==4 and i==5:
           print("*",end=" ")
        else:
             print(" ",end=" ")
    print()
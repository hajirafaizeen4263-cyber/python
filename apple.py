#print triangle with word apple
n="APPLE"
for i in range(len(n)) :
    for j  in range(len(n)-i-1):
        print(" ",end="  ")
    for k in range (i+1):
        print(n[k],end="    ")
    print()
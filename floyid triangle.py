#triangle floyid 
for i in range(1,9):
    for j in range(8-i):
        print("  ",end=" ")
    for k in range(i):
        print(f"{i+k:2}" ,end="   ")
    print()
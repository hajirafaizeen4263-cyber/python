#list

#collection of data
#a=[2,4,6,8]

#list can have any elements of any size
#a=[1,2.2,'mohan',True]
#properties

#lists are ordered

# a=[1,2,3,4]
# b=[4,3,2,1]
# print(a==b)

# a=[1,2,3,4,5]
# print(a[3])


# a=[4,3,2,1]
# print(a[0]==a[-4])

#[start:stop:step]


# a=[1,2,3,4,5,6,7,8,9]
# print(a[1:4])
# print(a[:6])
# print(a[4:])
# print(a[::])

#lists are dynamic
# a=[11,12,13,14,15]
# a[0:2]=[1,2,3,4,5]
# print(a)

# lists are nested

# a=[11,12,[100,300],15]
# print(a[2][1])

#inbuilt methods

#to add elements

# a=[11,12,13,14,15]

#append
# a.append(100)
# print(a)

#extend
# a.extend("hajira")
# print(a)

# a.extend([1,2])
# print(a)

#insert
# a.insert(3,4)
# print(a)

#to remove elements
#remove
# a.remove(11)
# print(a)

#pop()
# a.pop()
# print(a)

#pop(index)
# a.pop(0)
# print(a)



#tuple
#collection of data,ordered,indexed and immutable

# a=(1,2,3,4,5)
# a[0]=10
# print(a)

#2 boxes

#elastic box- list
#metal box-tuple


#loop

# fruits=["apple","orange","watermelon","banana","pineapple","mango"]
# for i in range(0,len(fruits)):
#     print(i)

# for i in range(0,len(fruits)):
#     print(i,fruits[i])
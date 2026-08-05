# list is a class
# list is a type
# list is an iterable
# list is a sequence
# list is mutable
# list elements are indexed
# list is growable
# list can contain heterogeneous elements
# list hamesh ek list object return karta hai

#creating list object
 
# l1=[10,20,30,2]
# print(l1)
# print(id(l1))
# print(id(l1[0]),id(l1[1]),id(l1[2]))
# print(type(l1))

# l2=['bhopal','pune','indore','patna']
# print(l2)
# print(type(l2))

# l3=[34,4.5,True,'abc',4+3j]
# print(l3)
# print(type(l3))

# # we can access also as index
# print(l1[0])
# print(l1[1])
# print(l1[2])
# # print(l1[3]) # IndexError: list index out of range

# for x in l1 :
#      print(x,end=" ")
# print("\n")






# Second Method to create list object
# list() - conversion function

# [] ye ek List object return karta hai

# x1=[10,20,30,40] 
# print(id(x1),id(x1[0]),id(x1[1]),id(x1[2]))


# list ek class hai and kisi v class name ke aage () lagane se conversion
# function(funtion call) ban jata hai
# and wo function ek new list ka object create karta hai and return karta hai


"""
x ──► list object
        │
        ▼
   ┌─────────────────────┐
   │ index │ reference   │
   ├───────┼─────────────┤
   │   0   │ ──► 12      │
   │   1   │ ──► 23      │
   │   2   │ ──► 45      │
   │   3   │ ──► 56      │
   └─────────────────────┘
"""

# x=list()
# print(x)
# print(id(x))
# print(type(x))
# x.append(10)
# print(x)

# #x1=list(10) # Error - List argument must be iterable 

# x1=list(range(5))

# x1=list('abc')
# print(x1)



#How to delete?
# del listObject[index]
#  index must be in valid range



# What is a class?
# Class is a group of variables and functions (known as attributes)
# how to access any member function of a class?
#listObject.memberFunction()


# add new element at the end of the list
#listObject.append(element)

# add new element at given index in the list
#listObject.insert(index,element)



# #packing
# a,b,c=1,2,3
# l2=[a,b,c]
# print(l2)

# #unpacking
# l3=['AB','AC','AD','AE']
# a,b,c,d=l3 # variable ki number utna ji rahna chaiye jitna object ke andar value hai
# print(a,b,c,d)




#Built-in methods. You can apply them on any iterable
# len(),sum(),max(),min(),sorted()

#sorted(listObject) - always return a list of listObject elements in sorted order

# ye list class ke object nahi hai isliye we can't access 
# with objectname . nahi kar sakte access

# l2=['a','b','c']
# print(len(l1))
# print(min(l1))
# print(min(l2))
# print(max(l2))
# #print(sum(l2)) # hma string ko nahi add kar sakte hai
# print(sorted(l1))
# l4=sorted(l1)
# print(sorted(l1,reverse=True))
# print(l1) # [10,20,30]


# l3=[10,2.5,True,10+5j,'rajneesh']
# print(max(l3)) # Error  not supported between instances of 'complex' and 'int'
#  not supported between instances of 'str' and 'int'


# x1=[1,2,3]
# x2=[2,3,1]
# print(x1==x2)
# print(x1>x2) # frist

# print(x1+x2)
# print(x1*3)


# #Slicing Operator
#listObject[beg:end:step]

# l1=[10,20,30,40,50,60,70,80,90,100]
# print(l1)
# print(l1[0:4:2]) #10 40
# print(l1[::])
# print(l1[::-1]) # reverse
# print(l1[5::-1])


# list methods

# l1=[1,56,12,23,78,56,54,52,31,65]
# l1.pop()
# print(l1) 
# l1.remove(12)
# print(l1)
# l1.sort()
# print(l1)
# print(l1.index(56)) # return index ,index(element)

# print(l1.count(100))
# print(l1.count(56)) 

# l1.reverse()
# print(l1)

# l1.append(200) # insert Last Position
# print(l1)

# l1.insert(2,500) # insert(index,element)
# print(l1)

# l1.clear()
# print(l1)


# x1=[x for x in range(1,6)]
# print(x1)

# Same Code

# x1 = []
# for x in range(1, 6):
#     x1.append(x)
# print(x1)

# x1=[x*2 for x in range(1,6)]
# print(x1)


# x1=[x**2 for x in range(1,6)]
# print(x1)


# x1=[1 for x in range(1,6)]
# print(x1)
# print(id(x1[0]),id(x1[1]),id(x1[2]),id(x1[3]))

# """
# x1
#  │
#  ▼
# [ * ][ * ][ * ][ * ]
#   │    │    │    │
#   └────┴────┴────┴──► PyIntObject(1)

# """

# x2=[12,23,45,56,89]
# print(id(x2[0]),id(x2[1]),id(x2[2]),id(x2[3]))



# Important Concept

# x=list([12,23,34])
# print(x)
# for y in list([12,23,45,56]): 
#     print(y,end=' ')

# for x in [12,23,45,56] :
#      print(x,end=' ')
# print("\n")





# List is Mutable
# l1=[12,23,56,45]
# l1[0]=122
# print(l1)





# 👉 Python list is a dynamic array of object references.
# It stores pointers, not actual values, and resizes automatically.

# ✅ Final Summary Table
# Operation	Best	Average 	Worst
# append(x)	O(1)	O(1) amortized	O(n)
# pop() (end)	O(1)	O(1)	        O(1)
# pop(i)        O(1)	O(n)	        O(n)
# (middle/front)

# remove(x)	O(1)	O(n)	        O(n)
# 🔥 Interview One-Liner




x=["rajneesh","bhopal","pune","indore"]
# print(x[0][1]) # r
# # print(x[1][0]) # b
# # for name in x:
# # for name in x:
# for y in range(len(x[0])) :
#         print(x[0][y],end=" --")
#         print("\n")

for i in x :
     print(i[0])           
# range is a class
# range is a type
# range is an iterable
# range is a sequence
# range object contains an arithmetic Progression (AP)
# range elements are always of type int
# step is by default 1
# single argument is always end value (consider beg=0)
# range object is immutable
# range object has a concept of indexing

# x=range(beg,end,step)
# 1) range(beg,end,step)

# range is not a referrence variable ,it is built-function that returns iterator object 
# thist iterator object is of type range
# iterator object is not a memory address , it is logical abstraction which helps to iterate over a sequence of values
 # range object,range iterator,range



x=range(1,10,2)
# print(x) # range(1, 10, 2)

range(1, 10, 2)

type(x)
#<class 'range'>


#type(range())
# TypeError: range expected at least 1 argument, got 0



# type(range(1))
#<class 'range'>


# print(y)
# for x in range(1,11,1) :
#      print(x)

# x=range(2,20,2)
# for y in x :
#      print(y,end=" ")
# print("\n")


# # 2) range(beg,end)  # step =1

# x=range(2,20)
# for y in x :
#      print(y,end=" ")
# print("\n")

# # 3) range(end) # beg=0, step=1

# x=range(20)
# for y in x :
#      print(y,end=" ")
# print("\n")



#-9-8-7-6 -5 -4 -3 -2 -1 (negative index)
# 0 1 2 3  4  5  6  7  8  (positive index)
# 2 4 6 8 10 12 14 16 18



# i=0
# while i<=8:
#     print(x[i],end=' ')
#     i+=1

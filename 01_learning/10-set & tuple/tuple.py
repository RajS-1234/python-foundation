# A tuple is an ordered collection of elements.
# tuple is a class
# tuple is a type
# tuple is an iterable
# tuple is a sequence
# tuple elements are indexed
# tuple is immutable
# tuple can contain values of different types


# how to create tuple object

print("Tuple Fundamentals")


# print("1.EMPTY TUPLE OBJECT")
# t1=() # empty tuple
# print(type(t1))


# print("2.TUPLE WITH MULTIPLE ELEMENTS")
# t2=(1,2,3,4,5) # Tuple with multiple elements
# print(type(t2))
# print(t2)


# # Tuple without parentheses
# print("3.TUPLE WITHOUT PARENTHESES")
# t5=10,20,30,40 #  This is called tuple packing.
# print(type(t5))
# print(t5)



# # Single-Element Tuple
# print("4.SINGLE-ELEMENT TUPLE") 
# t3=(10) # it is considered as int not tuple
# print(type(t3)) 
# print(t3)


# # To create a one-element tuple, use a comma

# t4=(10,) # single element tuple
# print(type(t4))
# print(t4)   



# Indexing
# Tuple indexing works exactly like list indexing.

# positive and negative indexing
# t6=(10,20,30,40,50)
# print(t6[0],t6[1],t6[2])
# print(t6[-1],t6[-2],t6[-3])













# 1. Tuple Packing

# Packing means putting multiple values into one tuple.

t = 10, 20, 30

print(t) # (10, 20, 30)  This is called packing.



# Tuple Unpacking ⭐⭐⭐

# Unpacking means extracting tuple values into variables.

student = ("Rajneesh", 21, "CSE")

name, age, branch = student

print(name) # Rajneesh
print(age) # 20
print(branch) # branch



"""

# Number of Variables Must Match
t = (10, 20, 30)

a, b, c = t 
✅ Correct.



a, b = t

# ❌ Error because there are 3 values but only 2 variables.

Similarly:

a, b, c, d = t

❌ Error.



"""



# Starred Unpacking ⭐⭐⭐

# Python allows *.

t = (10, 20, 30, 40, 50)

a, *b = t

print(a) # 10
print(b) # [20, 30, 40, 50]  Notice that b is a list, not a tuple.

# The starred variable receives a list, not a tuple.




# Another example

*a, b = (10, 20, 30, 40)

print(a) # [10, 20, 30]
print(b) # 40


# Middle unpacking

a, *b, c = (10, 20, 30, 40, 50)

print(a) # 10
print(b) # [20, 30, 40]
print(c) # 50





















# # Accessing tuple object

# #1)
# print(t6)

# #2)
# print(t6[0],t6[1],t6[2],t6[3])

# #3)
# for x in t6 :
#     print(x)

# #4)
# i=0
# while i < len(t6):
#     print(t6[i])
#     i += 1

  





#built-in methods
# len(), max(), min(), sorted()

# len()








# Tuple Concatenation

t7=(10,20,30)
t8=(40,50,60)
t9=t7 + t8 # concatenation
print(t9)
 
t10=t7*3 # Tuple Repetition
print(t10)

# t7[0]=100 # TypeError: 'tuple' object does not support item assignment
# print(t7)




# comparison and membership operators
# Python compares tuples element by element

# print(t7>t8) # False
# print(t7< t8) # True          
# print(t7==t8) # False
# print(t7!=t8) # True
# print(t7>=t8) # False
# print(t7<=t8) # True
# print(20 in t7) # True
# print(100 in t7) # False
# print(30 not in t7) # False
# print(100 not in t7) # True
# # --------------- IGNORE ------------------


# tuple methods
# count()
# index()


# 1) count() - Counts how many times an element occurs.
# t11=(10,20,30,10,20,10,10)
# c=t11.count(10)
# print(c) # 4



#2) index() Returns the first index where the value occurs.
t12=(10,20,30,40,50)
i=t12.index(30)
print(i) # 2


# You can also specify a starting position:
print(t12.index(20, 2)) #  .index(value, index) This will raise a ValueError because 20 is not found after index 2.





# # --------------- IGNORE ------------------


# # slicing operator
# # tupleObject[beg:end:step] # beg is inclusive , end is exclusive
# t13=(10,20,30,40,50,60,70,80,90)
# print(t13[2:7]) # (30, 40, 50, 60, 70)

# print(t13[::-1]) # (90, 80, 70, 60, 50, 40, 30, 20, 10)
# # agar hamne beg and end nahi diye to by default beg=0 and end=len(tupleObject)



# # --------------- IGNORE ------------------

# # user input tuple
# t1=tuple([int(x) for x in input("Enter multiple values separated by space: ").split(' ')])
# print(t1)




# tuple() Constructor
# You can convert another iterable into a tuple.

# t2=tuple()
# print(t2)

# t3=tuple(range(5))
# print(t3)

# t4=tuple('mysirg')
# print(t4)


# t5=tuple({1,2,3,4})
# print(t5)

# t6=tuple({'a':1,'b':2,'c':3})
# print(t6)

# t7=tuple((10,20,30))
# print(t7)

# t8=tuple([10,20,30])
# print(t8)

# # --------------- IGNORE ------------------



# Tuple and zip()

# Very useful in real programming.

# names = ("Rajneesh", "Amit", "Rahul")
# ages = (21, 22, 23)

# result = tuple(zip(names, ages))

# print(result)

# Output:

# (('Rajneesh', 21), ('Amit', 22), ('Rahul', 23))
# 32. Tuple and Function Return

# Functions can return multiple values.

# def get_student():
#     return "Rajneesh", 21, "CSE"

# result = get_student()

# print(result)

# Output:

# ('Rajneesh', 21, 'CSE')

# Python is effectively returning a tuple here.

# You can unpack it:

# name, age, branch = get_student()

# This is one of the most practical uses of tuples.


# Tuple Comprehension? ⭐⭐⭐

# Python does not have a tuple comprehension.

# This:

# t = (x for x in range(5))

# does not create a tuple.

# It creates a generator.

# print(type(t))

# Output:

# <class 'generator'>

# To create a tuple:

# t = tuple(x for x in range(5))

# print(t)

# Output:

# (0, 1, 2, 3, 4)












# Can a Tuple Contain Mutable Objects?

# Yes.

# This is an important interview concept.

# t = (10, [20, 30], 40)

# You cannot replace the list itself:

# t[1] = [50, 60]

# ❌ Error.

# But you can modify the list inside the tuple:

# t[1].append(40)

# print(t)

# Output:

# (10, [20, 30, 40], 40)

# Why?

# Because tuple immutability means:

# The tuple's references cannot be changed.

# It does not mean that every object reachable through the tuple must be immutable.

# Conceptually:

# tuple
#   |
#   +----→ 10
#   |
#   +----→ list
#           |
#           +----→ 20
#           +----→ 30

# The tuple still points to the same list object.
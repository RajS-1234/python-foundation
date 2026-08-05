# tuple is a class
# tuple is a type
# tuple is an iterable
# tuple is a sequence
# tuple elements are indexed
# tuple is immutable
# tuple can contain values of different types


# how to create tuple object

t1=() # empty tuple
print(type(t1))
t2=(1,2,3,4,5)
print(type(t2))
print(t2)

t3=(10) # it is considered as int not tuple
print(type(t3)) 

t4=(10,) # single element tuple
print(type(t4))


t5=10,20,30,40 # tuple packing
print(type(t5))
print(t5)


# positive and negative indexing
t6=(10,20,30,40,50)
print(t6[0],t6[1],t6[2])
print(t6[-1],t6[-2],t6[-3])


# Accessing tuple object

#1)
print(t6)

#2)
print(t6[0],t6[1],t6[2],t6[3])

#3)
for x in t6 :
    print(x)

#4)
i=0
while i < len(t6):
    print(t6[i])
    i += 1

  

#builtin methods
# len(), max(), min(), sorted()


# some operations on tuple

t7=(10,20,30)
t8=(40,50,60)
t9=t7+t8 # concatenation
print(t9)

t10=t7*3 # repetition
print(t10)

# t7[0]=100 # TypeError: 'tuple' object does not support item assignment
# print(t7)

# comparison and membership operators

print(t7>t8) # False
print(t7< t8) # True          
print(t7==t8) # False
print(t7!=t8) # True
print(t7>=t8) # False
print(t7<=t8) # True
print(20 in t7) # True
print(100 in t7) # False
print(30 not in t7) # False
print(100 not in t7) # True
# --------------- IGNORE ------------------


# tuple methods
# count()
# index()
# --------------- IGNORE ------------------

#1) count()
t11=(10,20,30,10,20,10,10)
c=t11.count(10)
print(c) # 4

#2) index()
t12=(10,20,30,40,50)
i=t12.index(30)
print(i) # 2

# --------------- IGNORE ------------------


# slicing operator
# tupleObject[beg:end:step] # beg is inclusive , end is exclusive
t13=(10,20,30,40,50,60,70,80,90)
print(t13[2:7]) # (30, 40, 50, 60, 70)

print(t13[::-1]) # (90, 80, 70, 60, 50, 40, 30, 20, 10)
# agar hamne beg and end nahi diye to by default beg=0 and end=len(tupleObject)



# --------------- IGNORE ------------------

# user input tuple
t1=tuple([int(x) for x in input("Enter multiple values separated by space: ").split(' ')])
print(t1)


t2=tuple()
print(t2)

t3=tuple(range(5))
print(t3)

t4=tuple('mysirg')
print(t4)


t5=tuple({1,2,3,4})
print(t5)

t6=tuple({'a':1,'b':2,'c':3})
print(t6)

t7=tuple((10,20,30))
print(t7)

t8=tuple([10,20,30])
print(t8)

# --------------- IGNORE ------------------
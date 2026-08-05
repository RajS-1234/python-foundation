#list is a class
#list is a type
#list is an iterable
#list is a sequence
#list is mutable
#list elements are indexed
#list is growable
# list can contain heterogeneous elements

#creating list object
l1=[10,20,30]

#How to access list elements?
print(l1)
print(l1[0],l1[1],l1[2])
for e in l1:
    print(e)

i=0
while(i<3):
    print(l1[i])
    i+=1
#How to delete?
del listObject[index]

#how to edit
listObject[index]=newValue

#index must be in valid range

# What is a class?
# Class is a group of variables and functions (known as attributes)
# how to access any member function of a class?
#listObject.memberFunction()

# add new element at the end of the list
listObject.append(element)

# add new element at given index in the list

listObject.insert(index,element)

#packing
a,b,c=1,2,3
l2=[a,b,c]

#unpacking
l3=['AB','AC','AD','AE']
a,b,c,d=l3

#Built-in methods. You can apply them on any iterable
# len(),sum(),max(),min(),sorted()

#sorted(listObject) - always return a list of listObject elements in sorted order

#Slicing Operator
listObject[beg:end:step]

#list methods
clear()
pop()
remove(element)
sort()
index(element)
count(element)
reverse()
append()
insert()


# List Comprehension
[ expression for var in iterable]
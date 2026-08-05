# set is a class
# set is a type
# set is an iterable
# set is not a sequence
# set has no concept of indexing
# set doesn't support slicing operator
# set cannot have duplicate values
# set can have values of different types but not list and set
# set is mutable



# how to create set object
s1={} # empty set
print(type(s1)) # dict - not set object
s1=set() # empty set
print(type(s1)) # set object

s2={1,5,8}
print(type(s2))
print(s2)




# set() - conversion function
print('--- Conversion to set ---')           
s3=set([1,2,3,4,5]) # from list              
print(type(s3))
print(s3)


s4=set((10,20,30,40)) # from tuple
print(type(s4))
print(s4)



s5=set({100,200,300}) # from set
print(type(s5))
print(s5)



s6=set('mysirg')      # from string
print(type(s6))
print(s6)



# Accessing set object
#1)
print(s2)

#2)
for x in s2 :
    print(x)

# no indexing and slicing in set beacause set is unordered collection of items
# so we cannot access set elements using indexing and slicing
# set implement in binary search tree internally

# builtin methods
# len(), max(), min(), sorted()




# some operations on set
s6={1,2,3,4,5}
s7={4,5,6,7,8}

# concatination and repetition are not supported in set

# comparision oerators

# print(s6==s7) # False
# print(s6!=s7) # True
# print(s6<s7)  # False
# print(s6>s7)  # False
# print(s6<=s7) # False
# print(s6>=s7) # False

# membership operators

# print(3 in s6)  # True
# print(10 in s6) # False
# print(4 not in s7) # False
# print(20 not in s7) # True


# set methods

s8={1,2,3,4,5}
s9={4,5,6,7,8}

#1) add() - adds single element to set 
s8.add(10)
print(s8) # {1, 2, 3, 4, 5, 10}

#2) update(iterable) - adds multiple elements to set
s8.update([20,30,40])
print(s8) # {1, 2, 3, 4, 5, 10, 20, 30, 40}

#3) remove(element) - removes specified element from set, raises KeyError if element not found
s8.remove(10)
print(s8) # {1, 2, 3, 4, 5, 20, 30, 40}

#4) discard(element) - removes specified element from set, does not raise error if element not found
s8.discard(100) # no error
print(s8) # {1, 2, 3, 4, 5, 20, 30, 40}


#5) pop() - removes and returns an arbitrary element from set
e=s8.pop()
print(e)
print(s8) 

#6) union(set) - returns a new set with elements from both sets
s10=s8.union(s9) # it does not modify original sets and returns new set and give unique elements
print(s10) # {1, 2, 3, 4, 5, 6, 7, 8, 20, 30, 40}


#7) intersection(set) - returns a new set with elements common to both sets
s11=s8.intersection(s9) # it does not modify original sets and returns new set
print(s11) # {4, 5}


#8) issubset(set) - checks if current set is subset of given set
print(s11.issubset(s8)) # True
print(s8.issubset(s11)) # False

#9) issuperset(set) - checks if current set is superset of given set
print(s8.issuperset(s11)) # True
print(s11.issuperset(s8)) # False


#10) difference(set) - returns a new set with elements in current set but not in given set
s12=s8.difference(s9) # it does not modify original sets and returns new set
print(s12) # {1, 2, 3, 20, 30, 40}

#11) clear() - removes all elements from set
s8.clear()     
print(s8) # set()



# set comprehension

s13={x*x for x in range(1,11)}
print(s13) # {1, 4, 36, 9, 16, 49, 25, 64, 100, 81}


# user input set
s14={x for x in input("Enter a Number of values separated by comma: ").split(',')}
print(s14)


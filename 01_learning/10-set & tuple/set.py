# 1. Set Fundamentals

# set is a class
# set is a type
# set is an iterable
# set is not a sequence
# set has no concept of indexing
# set doesn't support slicing operator
# set cannot have duplicate values
# set can have values of different types but not list and set
# set is mutable



# Creating Sets

# s1={} # empty set
# print(type(s1)) # dict - not set object
# s1=set() # empty set
# print(type(s1)) # set object

# s2={1,5,8}
# print(type(s2))
# print(s2)




# set() - conversion function
# 3. Creating Set from Other Iterables

        
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


# 4. Set Elements / Hashability
# A set can contain hashable objects.

# A hashable object has a hash value which remains the same during its lifetime.
my_set = {     
     10,   # int
     3.14, # float
     "hello", # string
     True,  # boolean
     (1, 2, 3), # tuple
     frozenset({4, 5, 6}), # frozenset  # deep dive into frozenset in next section
}


# invalid set elements

# my_set = {
#     [1, 2, 3],
#     {4, 5, 6},
#     {'a': 1, 'b': 2},
# } # list and set are unhashable and cannot be added to a set

"""

why? Because list and set are mutable objects, 
their hash value can change during their lifetime,
which violates the requirement for hashable objects to have a constant hash value.
Therefore, they cannot be added to a set, which requires all elements to be hashable.

"""
               
# set = {(1,2,3)}
# {(1,[2,3])} # TypeError: unhashable type: 'list'    






# 5. Set is Mutable

# You can change the set after creation.

s = {1, 2, 3}
s.add(4)
print(s)

# But individual set elements cannot be modified because sets don't expose elements by index.




# 6. Set Does Not Support Indexing

s = {10, 20, 30}
# print(s[0]) 

"""
❌ Error:

TypeError: 'set' object is not subscriptable

Why?

Because a set is unordered and doesn't provide positional indexing.

"""



# 7. Adding Elements
# add()

# s = {1, 2, 3}
# s.add(4)
# print(s)

# If the element already exists:

# s.add(3)
# print(s)  # {1, 2, 3, 4} - no duplicates allowed

# Nothing happens.







# 8. Adding Multiple Elements


# update() # You can pass different iterables:
s = {1, 2}

s.update([3, 4, 5])

print(s)

s.update((6, 7))
s.update({8, 9})
s.update("ab")
s.update({10: "ten", 11: "eleven"})  # Only keys are added
print(s)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 'a', 'b'}




# 9. Removing Elements

# There are several important methods.

# remove()
s = {1, 2, 3}

s.remove(2)
print(s)

# If element doesn't exist:

# s.remove(10) # keyError

# ❌ KeyError

# discard()
s.discard(2) # No error.

# If element doesn't exist:

# s.discard(10)

# No error.




# pop() removes and returns an arbitrary element.

# Don't assume it removes the first or last element.
# 10. pop() # deletes and returns an arbitrary element from the set. Since sets are unordered, you cannot predict which element will be removed.
s = {10, 20, 30, 40, 50}

x = s.pop()
print(x)
print(s.pop())

print(s)



s = {1, 2, 3}

s.clear()

print(s)
print(type(s)) # <class 'set'> - empty set object
# set()




# 12. Set Length
s = {10, 20, 30}

print(len(s))





# 13. Membership Testing

# One of the most important uses of sets.

s = {10, 20, 30}

print(20 in s)
print(50 in s)

# Output:

# True
# False

# This is usually very efficient because sets use hash tables internally.

# Average-case:

# x in set → O(1)





# Accessing set object
#1)
# print(s2)

# #2)
# for x in s2 :
#     print(x)

# no indexing and slicing in set beacause set is unordered collection of items
# so we cannot access set elements using indexing and slicing
# set implement in binary search tree internally

# builtin methods
# len(), max(), min(), sorted()




# some operations on set
# s6={1,2,3,4,5}
# s7={4,5,6,7,8}

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

# s8={1,2,3,4,5}
# s9={4,5,6,7,8}

# #1) add() - adds single element to set 
# s8.add(10)
# print(s8) # {1, 2, 3, 4, 5, 10}

# #2) update(iterable) - adds multiple elements to set
# s8.update([20,30,40])
# print(s8) # {1, 2, 3, 4, 5, 10, 20, 30, 40}

# #3) remove(element) - removes specified element from set, raises KeyError if element not found
# s8.remove(10)
# print(s8) # {1, 2, 3, 4, 5, 20, 30, 40}

# #4) discard(element) - removes specified element from set, does not raise error if element not found
# s8.discard(100) # no error
# print(s8) # {1, 2, 3, 4, 5, 20, 30, 40}


# #5) pop() - removes and returns an arbitrary element from set
# e=s8.pop()
# print(e)
# print(s8) 

# #6) union(set) - returns a new set with elements from both sets
# s10=s8.union(s9) # it does not modify original sets and returns new set and give unique elements
# print(s10) # {1, 2, 3, 4, 5, 6, 7, 8, 20, 30, 40}


# #7) intersection(set) - returns a new set with elements common to both sets
# s11=s8.intersection(s9) # it does not modify original sets and returns new set
# print(s11) # {4, 5}


# #8) issubset(set) - checks if current set is subset of given set
# print(s11.issubset(s8)) # True
# print(s8.issubset(s11)) # False

# #9) issuperset(set) - checks if current set is superset of given set
# print(s8.issuperset(s11)) # True
# print(s11.issuperset(s8)) # False


# #10) difference(set) - returns a new set with elements in current set but not in given set
# s12=s8.difference(s9) # it does not modify original sets and returns new set
# print(s12) # {1, 2, 3, 20, 30, 40}

# #11) clear() - removes all elements from set
# s8.clear()     
# print(s8) # set()



# # set comprehension

# s13={x*x for x in range(1,11)}
# print(s13) # {1, 4, 36, 9, 16, 49, 25, 64, 100, 81}


# # user input set
# s14={x for x in input("Enter a Number of values separated by comma: ").split(',')}
# print(s14)


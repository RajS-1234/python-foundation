# filter
# filter() function is used to filter elements from an iterable (like a list or tuple) based on a specified condition defined by a function.
# syntax : filter(function, iterable)
# function : a function that defines the condition to be applied to each element of the iterable. It should return True or False.
# iterable : an iterable (like a list, tuple, etc.) whose elements will be filtered based on the function.
# return value : filter object (an iterator) that can be converted to a list, tuple, or other iterable types.
# filter object is lazy evaluated (elements are computed on demand)
# filter is commonly used for selecting specific elements from a collection based on certain criteria.

def isEven(n) :
     if(n%2==0) :
         return n
     
x=filter(isEven,[1,2,3,4,5,6,7,8,9,10]) # filter object
print(list(x)) # [2, 4, 6, 8, 10]
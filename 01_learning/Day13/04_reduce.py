# reduce
# reduce() function is used to apply a function to the elements of an iterable (like a list or tuple) and return a single value.
# syntax : reduce(function, iterable)
# function : a function that defines the operation to be applied to the elements of the iterable.
# iterable : an iterable (like a list, tuple, etc.) whose elements will be processed by the function.
# return value : a single value that is the result of applying the function cumulatively to the elements of the iterable.
# reduce is commonly used for aggregating data or performing operations like summing numbers or finding maximum values.


# syntax : reduce(function, iterable, initializer=None)
# function : a function that takes two arguments and returns a single value.
# iterable : an iterable (like a list, tuple, etc.) whose elements will be processed by the function.
from functools import reduce



x=reduce(lambda a,b:a+b,[1,2,3,4,5]) # 15
# print(list(x)) # TypeError: 'int' object is not iterable
print(x)

y=reduce(lambda a,b:a*b,[1,2,3,4,5],initial=10) # 120
print(y)       
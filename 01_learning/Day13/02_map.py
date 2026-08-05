# map,reduce,filter

# high order function : function which take function as argument or return function as return value      

# map
# map() function is used to apply a function to each element of an iterable (like a list or tuple) and return a new iterable with the results.
# syntax : map(function, iterable) 
# function : a function that defines the operation to be applied to each element of the iterable.
# iterable : an iterable (like a list, tuple, etc.) whose elements will be processed by the function.
# return value : map object (an iterator) that can be converted to a list, tuple, or other iterable types.
# map object is lazy evaluated (elements are computed on demand)
# map is commonly used for transforming data in a concise and efficient manner.



# map(function, iterable)
# ye address return  nahi karta hai ye iterator return karta hai jo logically container ke element ko access karta hai


def fun(x) :
    return x*x
x=map(fun,[1,2,3,4,5]) # x is map object, return function object
print(x)
print(type(x))

# converting map object to list
y=list(x)
print(y)
# for i in x :
#     print(i)  # no output because map object is exhausted after converting to list



def isPrime(n) :
    if n<2 :
        return False
    for i in range(2,n) :
        if n%i==0 :
            return False
    return True

print(list(map(isPrime,[10,15,23,36,47,55,60,73])))
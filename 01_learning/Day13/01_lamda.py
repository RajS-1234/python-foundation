def add(a,b) :
    return  a+b

x=add
print(x(10,10))

"""
what is add ?
add is reference variable which is refer to the function object

what is different between add and add() ?
add refer to function object
add() is function call 

"""
# lamda is single line of expression function which is defined by lamda keyword
# syntax : lambda argument1, argument2,... : expression 
# lamda function always return value of expression
# lamda function is also called anonymous function because it does not have any name 
# lamda is a keyword in python

x=lambda a,b:a+b 
print(id(x))
print(x)
result=x(10,20)
print(result)


print("--------------------------------------------------")

# Example 2 : lamda function with single argument
print((lambda a:a*a)(5)) # 25


def square(mylsit,fun) :
     for x in mylsit :
         print(x,fun(x)) 

square([1,2,3,4,5],lambda x:x*x)

#  labda maxium use case with builtin functions like map(), filter(), reduce() for data manipulation


# variable length keyword arguments

def f1(*t) : # t is tuple
    print(t)
    print(type(t))

f1(10,20,30)


def f2(**k) :  # k is dict
     for key in k :
         print(key,k[key])


f2(a=10,b=20,c=30)
# way to define functions in python
# function is a block of code which performs a specific task

def f1() :
     a=10
     b=30
     print("Sum is",a+b)

# f1 is function name and it is also a reference variable which refers to function object

print(f1)
x=f1

# How to call a function?

x() # function call
f1() # function call


def f1() :
   a=10  
   b=20
   c=30
   print("Average is",(a+b+c)/3)
x=f1()  # function call
print(x) # None







#1) Takes Nothing, Returns Nothing
def add1():
    print("Enter two numbers")
    a,b=int(input()),int(input())
    c=a+b
    print("Sum is",c)

#2) Take Something, Returns Nothing
def add2(a,b):
    c=a+b
    print("Sum is",c)

#3) Takes Nothing, Return Something
def add3():
    print("Enter two numbers")
    a,b=int(input()),int(input())
    c=a+b
    return c

#4) Take Something, Return Something
def add4(a,b):
    c=a+b
    return c
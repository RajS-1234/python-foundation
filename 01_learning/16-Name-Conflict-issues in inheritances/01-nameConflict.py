#Instance Object variable name conflict

# Case 1 — Parent and Child both use the same variable name



# When a child class inherits from a parent class, the child gets access to the parent's methods and class attributes. But the parent's instance variables are created only when the parent's __init__() runs.
# If the parent has an __init__() and the child calls super().__init__(), the parent's instance variables are created inside the child object.




class Parent :
    def __init__(self):
        self.x=10
class Child(Parent):
    def __init__(self):
        self.x=20



p=Parent() # 5
print(p.x)   

# whenever do'nt call the parent class then
#  in child class object have never create a instance member variable 
c=Child() # 4
print(c.x)

"""

Why?

Because Child.__init__() does:

self.x = 20

The self refers to the Child object.

So:

Child object
┌─────────────┐
│ x = 20      │
└─────────────┘

The Parent's __init__() was never called.

"""


# Case 2 — Child calls Parent's constructor


# class Parent :
#     def __init__(self):
#         self.x=10
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.x=20


# c=Child()
# print(c.x)

    
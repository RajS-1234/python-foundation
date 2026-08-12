
# 1. Variable Creation

"""
Python does not require us to declare the type of a variable.

We simply assign a value:

age = 21

        ┌─────────┐
age ───►│   21    │
        └─────────┘
          object


Python creates the object 21 and makes the name 'age'
refer to that object.
"""


"""    
        ┌─────────┐
age ───►│   21    │
        └─────────┘
          object

Python creates the integer object 21 and makes age refer to it.  
       
"""


age = 21
print(age)

x=3.5
print(x)

x="i am string"
print(x)


"""
print(y)  # koi v varible tab hi exit karega jab wo assigment ke left me ho

x=y
print(x)  yaha par name error aayega kyu ki variable banane ka rule hai  varible left
          side me rahna chahiye, agar right me hoto wo variable pahle se define ho 

Important

Python variables don't have a fixed type.
The object has the type, not the variable name.
"""


del(age)
# print(age) # age variable delete it is not exit




# 2. Variable Assignment

x = 10
print(x)
print(type(x))
print(id(x))


x = 20
print(x)
print(type(x))
print(id(x))   

"""
The important point is that = does not mean "put 20
inside a box called x" in the way beginners often imagine.

Make the name x refer to the object 20.
"""



# 3. Multiple Assignment

x, y, z = 10, 20, 30
print("x=",x,"y=",y,"z=",z)
print("x=",id(x),"y=",id(y),"z=",id(z))        


"""
x ───► 10

y ───► 20

z ───► 30

"""


# You can also assign the same object to multiple names:


x = y = z = 100
print("x=",x,"y=",y,"z=",z)
print("x=",id(x),"y=",id(y),"z=",id(z)) 

"""
       ┌───────┐
x ────►│       │
y ────►│  100  │
z ────►│       │
       └───────┘
       
"""



a = 10
b = 20

print("a=",a,"b=",b)
print("a=",id(a),"b=",id(b))  

a, b = b, a

print("a=",a,"b=",b)
print("a=",id(a),"b=",id(b))



# 5. Dynamic Typing

x = 10   # x refers to an integer object.
print(type(x))
print(id(x))


x = 3.5  # Now x refers to a float object.
print(type(x))
print(id(x))


x="i am string" # Now x refers to a string object.
print(type(x))
print(id(x))

x= True  # Now x refers to a boolean object.
print(type(x))
print(id(x))


"""
The variable doesn't permanently have a type. 
It can refer to an object of any type, and the type can change over time.

Python is dynamically typed because variable types are determined at runtime,
 and a variable can refer to objects of different types during its lifetime.

"""



# 6. Strong Typing

"""

Python is also strongly typed.

This means Python generally doesn't silently convert incompatible types just because an operation might seem convenient.

"""
# For example:

age = 20
name = "Raj"

result = age + name  # TypeError

# Python doesn't automatically decide:

# 20 + "Raj"
#       ↓
# "20Raj"

# Instead, you need to explicitly convert:

# result = str(age) + name

# Now:

# "20Raj"



# Dynamic vs Strong Typing

# These are different concepts.

# Concept	Meaning
# Dynamic typing	Type is determined at runtime
# Strong typing	Incompatible types aren't freely mixed

# Python is:

# Dynamically typed + strongly typed




# 7. Object References

x = 10

"""
Don't think:

x = box containing 10

Think:

x ─────► 10
        object

x is a reference/name pointing to an object.

"""

y = x  # y now refers to the same object as x.
print("x=",x,"y=",y)
print(x is y)

"""
x ────┐
      ↓
     10
      ↑
      |
y ────┘

"""



# 10. The Most Important Mental Model

# Remember this:

#              PYTHON
#                 │
#                 ↓
#         ┌─────────────────┐
#         │      Object     │
#         │                 │
#         │ value + type    │
#         └────────┬────────┘
#                  ↑
#                  │
#               reference
#                  │
#                  │
#               variable

# For:

# name = "Rajneesh"

# Think:

# name ─────────► "Rajneesh"
                │
  






# y=5
# print(type(y))
# print(id(y))

# y=5.5
# print(type(y))
# print(id(y))

# x="string"
# print(type(x))
# print(id(x))

# y='string'
# print(type(y))
# print(id(y))


# z="""string"""
# print(type(z))
# print(id(z))

# y=True
# print(y)
# print(type(y))
# print(id(y))




# Python me ek variable ke andar kisi bhi datatype ka value store ho sakta hai.

# 🔹 Reason: Python is dynamically typed

# Python me variable ka datatype fix nahi hota.
# Datatype value ke saath attach hota hai, variable ke saath nahi.

# 🔹 Example
# x = 10        # int
# print(x)

# x = 3.5       # float
# print(x)

# x = "Hello"   # string
# print(x)

# x = [1, 2, 3] # list
# print(x)


# 👉 Same variable x
# 👉 Different-different datatype values

# 🔹 Internally kya hota hai (important)

# Variable sirf reference (address) store karta hai

# Value memory me object ke form me hoti hai

# Har object ke paas:

# value

# datatype

# reference count

# Jab tum likhte ho:

# x = 10


# 10 ek int object banta hai

# x us object ka address point karta hai

# Phir:

# x = "Hi"


# "Hi" ek string object banta hai

# x ab naye object ko point karta hai

# Purana 10 object free ho sakta hai (GC ke through)

# 🔹 Isliye possible hai

# Python me:

# Variable = name

# Datatype = object ka property



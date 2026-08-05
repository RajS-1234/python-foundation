x=5
print(x)

x=3.5
print(x)

x="i am string"
print(x)

"""
print(y)  # koi v varible tab hi exit karega jab wo assigment ke left me ho

x=y
print(x)  yaha par name error aayega kyu ki variable banane ka rule hai  varible left
          side me rahna chahiye, agar right me hoto wo variable pahle se define ho 
"""

del(x)
# print(x) # x varible delete it is not exit


y=5
print(type(y))
print(id(y))

y=5.5
print(type(y))
print(id(y))

x="string"
print(type(x))
print(id(x))

y='string'
print(type(y))
print(id(y))


z="""string"""
print(type(z))
print(id(z))

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



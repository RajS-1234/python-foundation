# dict is a class
# dict is a type
# dict is an iterable
# dict is hashable 
# dict is not a sequence
# dict is mutable
# Each element in a dict is a pair of Key-Object
# Keys in dict must be unique (duplicate keys are not allowed)
# no concept of indexing
# no support of slicing operator
# unsupported concatenation operator, repetition operator and inequality operator

# How to create dict object 

# d1={} # empty dict
# print(type(d1))


# d2={102:'Rahul',103:'Sonam',104:'Anjali'}
# print(d2)

# d3={'name':'Ravi','age':25,'city':'Pune'}
# print(d3)

# # Accessing dict object
d3={'name':'rajneesh','age':21,'city':'bihar' ,'email':'rajneesh@gmail.com'}

# #1)
# print(d3)

# #2)
# print(d3['name'],d3['age'],d3['city'],d3['email'])

#3)
for key in d3 :
    print(key) # only keys

#4)
for key in d3 :
    print(key,d3[key])


# How to edit dict object
# dictObject[key-value]=newValue
#              
d3['age']=22 # updating existing key-value pair
print(d3)


del d3['city'] # deleting key-value pair
print(d3)

# How to add new key-value pair in dict object
d3['phone']=9876543210
print(d3)


# dict methods 
# keys(), values(), items(), get(), clear(), copy(), pop(), popitem(), update()
# print(dir(dict)) # list of all attributes of dict class

print("dict method",end="\n\n")

#1) keys()
d4={'name':'Ravi','age':25,'city':'Pune'}    
print(d4.keys()) # dict_keys object


#2) values()
print(d4.values()) # dict_values object


#3) items()
print(d4.items()) # dict_items object
for x in d4.items() :
    print(x)



print("\n\n")
# builtin functions
# len(), max(), min(), sorted()

map={
    'a':1,
    'b':2,  
    'c':3
}
print(sorted(map.keys(), reverse=True))     # sorted by keys
print(sorted(map.values(), reverse=True)) # sorted by values
print(sorted(map.items(), key=lambda x: x[1], reverse=True)) # sorted by key-value pair (first by key and then by value)


















data = {
    "name": ["Raj", "Sonu", "Kajal"],
    "age": [21, 22, 23]
}

# 1. Access full list
# print(data["name"])
# 2. Access single element from list
# print(data["name"][0])

# 3. Loop through list inside dict
# for n in data["name"]:
#     print(n)





# data = {
#     "students": [("Raj", 21), ("Sonu", 22), ("Kajal", 23)]
# }

# 1. Access full list
# print(data["students"])
# 2. Access one tuple (by index)
# print(data["students"][0])

# 👉 Output:

# ('Raj', 21)
# 3. Access value inside tuple
# print(data["students"][0][0])  # Name
# print(data["students"][0][1])  # Age

# 👉 Output:

# Raj
# 21
# 🔥 Loop (best way)
# for student in data["students"]:
#     print(student[0], student[1])
# 🔥 Best (clean code)
# for name, age in data["students"]:
#     print(name, age)

# 👉 Output:

# Raj 21
# Sonu 22
# Kajal 23
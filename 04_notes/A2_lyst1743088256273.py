# str is a class
# str is a type
# str is an iterable
# str is a sequence
# str elements are indexed
# str is immutable

#Creating string object
s1="mysirg"
s2='mysirg'
s3='''mysirg'''
s4="""mysirg"""

s5=str()
s6=str(125)
s7=str(4.5)

# Positive and negative indexing
#Accessing str object
#1) 
print(s1)
#2) 
print(s1[0],s1[1],s1[2])
#3)
for e in s1:
    print(e)

#4)
i=0
while i<len(s1):
    print(s1[i])
    i+=1
#5) 
s1[1:5:2] # strObject[beg:end:step]

#Builtin methods
# len(), max(),min(),sorted()

#str methods
index()
count()
startswith()
endswith()
isdigit()
isalpha()
lower()
upper()
islower()
isupper()
replace()
split() # returns a list of strings splitted on the basis of given string 
join()  # ','.join(list of strings)
format()


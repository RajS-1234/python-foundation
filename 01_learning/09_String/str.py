# str is a class
# str is a type
# str is an iterable
# str is a sequence
# str elements are indexed
# str is immutable

#---------------------------------------------------------------
# Creating string object

s1="MySirG"
s2='mysirg'
s3='''mysirg'''
s4="""mysirg"""

# Second Method to create str onject
# str() - conversion function

# s4=str()
# print(s4)


# s5=str(True)
# print(s5)


# s6=str(125)
# print(s6)


# s7=str(4.5)
# print(s7)


#----------------------------------------------------------------

# Positive and negative indexing
# Accessing str object

print(s1[-1]) # G
print(s1[-2]) # r


# #acess

#1)
print(s1)

#2)
print(s1[0],s1[1],s1[2],s1[3])

#3)
for x in s1 :
    print(x)

#4)
i=0
while(i<len(s1)) :
    print(s1[i])
    i+=1

#5)
s1[1:5:2] # strObject[beg:end:step]


# Some operation on str

# print('ab'+'ac')
# print("ab"*3)
# print('abc'>'aba')


#Builtin methods
# len(), max(),min(),sorted()



#str methods

# index()
# count()
# startswith()
# endswith()
# isdigit()
# isalpha()
# lower()
# upper()
# islower()
# isupper()
# replace()
# split() # returns a list of strings splitted on the basis of given string 
# join()  # ','.join(list of strings)
# format()

print("---------str methods--------")

#1) index(element)
print(s1.index('S')) # 2 
#print(s1.index('Z')) # # if element not found then ValueError


#2) count(element)  // Output True and False
print(s1.count('M')) # 1


#3) startswith()
print(s1.startswith('M')) # True


#4) endswith()
print(s1.endswith('g')) # False


#5) isdigit()
print(s1.isdigit()) # False


#6) isalpha()
print(s1.isalpha()) # True


#7) lower()
print(s1.lower()) # mysirg
print(s1) # lower() does not modify original string ,creates new string


#8) upper()
print(s1.upper()) # MYSIRG


#9) islower()
print(s1.islower()) # False


#10) isupper()
print(s1.isupper()) # False

#11) replace(oldChar,newChar)
print(s1.replace('M','m')) # mysirg
print(s1) #  replace() does not modify original string ,creates new string


#12) split()  # returns a list of strings splitted on the basis of given string

# s3="MySirG Education Services"
# l1=s3.split(" ")     # hamesh list of string  return karta hai ,split karne ka rijan hamesh ek nahi hota diff char and strig
# print(l1) # ['MySirG', 'Education', 'Services']
# print(type(l1)) # <class 'list'>
# # Each word is an element of list
# # Accessing list elements
# print(l1[0]) # MySirG
# print(l1[1]) # Education
# print(l1[2]) # Services
# # print(l1[3]) # IndexError: list index out of range


# a,b=int(input()),int(input())


# #list of string return karta hai split()
# print("Enter few numbers separated by comma")
# s=input()
# # s='10,34,21,56,78,45,50'
# l1=s.split(',')
# # l1 = ['10','34','21',56','78','45','50']
# l2=[]
# for x in l1:
#     l2.append(int(x))
# print(l2)

# # l2=[10,34,21,56,78,45,50]

# l2=[int(x) for x in input("Enter few numbers separated by comma").split(',')]




#13) join()  # ','.join(list of strings)

# l1=['MySirG', 'Education', 'Services']
# s4='-'.join(l1)
# print(s4) # MySirG-Education-Services


# print("Enter a string :")
# l1=input().split()
# s5=' '.join(l1)
# for x in s5:
#     print(x)


#14) format()
s6="MySirG {} {}"
print(s6.format("Education","Services")) # MySirG Education Services





# # str is immutable
# s1="rajneesh"
# s1[0]='m'
# print(s1)


# """
#  s1[0]='m'
#     ~~^^^
# TypeError: 'str' object does not support item assignment

# """

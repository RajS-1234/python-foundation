import keyword
print(keyword.kwlist)
print(keyword.softkwlist)

#How many data types you know?
# All the data types in Python are classes
# there are some data types, which are predefined and we can also define data type
#No data type is a keyword

#Type Conversion Functions
int()
float() 
complex()
str()
bool()

#Number System
"""
Binary      0,1
Octal       0,1,2,3,4,5,6,7
Decimal     0,1,2,3,4,5,6,7,8,9
Hexadecimal 0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f

Decimal 25  - Binary 11001
Decimal 25  - Octal 31
Decimal 25  - Hexadecimal 19

bin()
oct()
hex()

binary      0b10101
octal       0o123
hexadecimal 0x19

ord(character) --> unicode
chr(unicode)   --> character
"""

"""
Taking input from user

1) input()   ---> str
2) input(string) ---> str

a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=a+b
print("Sum is",c)

"""

# Types only variable ka nahi hota hai constant ka bhi hota hai
print(type(5))
# print(5+'3') # + operator does'nt no how to add two diffrent data types

# 5+'3'
"""
 Traceback (most recent call last):
   File "<pyshell#0>", line 1, in <module>
    5+'3'
   TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

5+3
8
5+int('3')
8

str(5)+'3'
'53'

# 1. ------Type - Conversion Diffrent Data types into int ------------------------------------------
a='123'
b=int(a)
b
123
type(a) 
#<class 'str'>
type(b)
#<class 'int'>


a='12x'
b=int(a)

"""
  Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b==int(a)
  ValueError: invalid literal for int() with base 10: '12x'
"""

# float Number
a=3.4
b=int(a)
b
3

# Bool Number
a=True
b=int(a)
b
# 1


a=False
b=int(a)
b
0

# Complex Number
a=3+4j
b=int(a)
"""
    Traceback (most recent call last):
    File "<pyshell#34>", line 1, in <module>
    b=int(a)
   TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
"""
 

# 2. ------Type - Conversion Diffrent Data types into str ------------------------------------------


# int 
a=12
b=str(a)
b
'12'

# Bool
a=True
b=str(a)
b
'True'

a=False
b=str(a)
b
'False'

# Float
a=2.3
b=str(a)
b
'2.3'

# Complex
a=4+4j
b=str(a)
b
'(4+4j)'


# 3. ------Type - Conversion Diffrent Data types into bool ------------------------------------------
a=12
b=bool(a)
b
True


a=3+4j
b=bool(a)
b
True

a='Rajneesh'
b=bool(a)
b
True


a=True
b=complex(a)
b
(1+0j)

a=False
b=complex(a)
b
0j


#------Type - Conversion Diffrent Data types into Complex ------------------------------------------

a=12
b=complex(a)
b
(12+0j)

a=12.12
b=complex(a)
b
(12.12+0j)

a='123'
b=complex(a)
b
(123+0j)

a='Rajn'
b=complex(a)
"""
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    b=complex(a)
ValueError: complex() arg is a malformed string

"""

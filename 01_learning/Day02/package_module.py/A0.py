# i want to acess variable a and b from module A1
# Remember module ko ham only file ke name se janenge uske end me ham .py na use karenge
import A1
print(A1.a, A1.b)

from A1 import a, b
print(a, b)

from A1 import *
print(a, b)

from A1 import a as first_number, b as second_number
a=100
b=200
print(a, b)
print(first_number, second_number)


# i am using module that is not exit in my file

import keyword
print(keyword.kwlist)
print(keyword.softkwlist)



# How to check Keyword on Shell
help() # in terminal types keywords

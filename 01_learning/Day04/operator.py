# Airthematic Operators
a=5
b=a**10
print(b)

a=-2
b=a**3
print(b)

a=(-2)**3
print(a)
print((-2)**2)

a=2**-2
print(a)

# // Floor Division
print("----Floor Division----")
a=15//2
print(a)
a=15.0//2
print(a)
a=15//2.0
print(a)
a=15.0//2.0
print(a)

# important concept
print("-----Floor Division Important Concept----")
print(123//10)
print(1234//100)
print(1234//1000)

# % Modulus Operator
print("----Modulus Operator----")
a=15%2
print(a)
a=15.5%2       
print(a)
a=15%2.5
print(a)
a=15.5%2.5
print(a)

# important concept how to check Divisible or not
print("----Modulus Important Concept----")
print(20%5)  # if remainder is 0 then number is divisible
print(20%3)  # if remainder is not 0 then number is not divisible


# Division Operator
print("----Division Operator----")
a=15/2
print(a) # it always return float value

# Addition Operator
print("----Addition Operator----")
print(5+2)
print("Rajneesh"+"Kumar")

# Relational Operators
print("----Relational Operators----")

# ==(Equal to), !=(Not Equal to), Never give Error
print(5>2)
print(5<2)
print(5>=2)
print(5<=2)
print(5==2)
print(5!=2)

print("raj">"kumar")
#print("raj">123) # it will give error str and int cant be compared

# both are Correct it give result as True and False
print("raj"=="raj") 
print("raj"!="kumar")

# Logical operator
print("----Logical Operators----")

print(not False)
print(not True)
print(not "rajneesh") # non empty string is True so not True is False
print(not "")         # empty string is False so not False is True
print(not 0)        # 0 is False so not False is True
print(not 5)        # non zero is True so not True is False
print(not None)     # None is False so not False is True


# or operator

print("----or Operator----")

print(3>4 or 5>0)
print(3>4 or 5>10)
print(4 or 3)
print( 0 or 5)
# and operator

print("----and Operator----")
print(3>4 and 5>0)
print(4>2 and 3>4)
print(4 and 3)
print(0 and 5)
print(5 and 0)
print(0 and 0)



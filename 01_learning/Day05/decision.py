# if Statement
a = 33
b = 200
if b > a:
  print("b is greater than a")


# if-else Statement
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# elif Statement
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")  



# Nested if 
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")    


# pass
a = 33
b = 200

if b > a:
  pass
else :
  pass




# Conditional operator
# value_if_true if condition else value_if_false
number = 10
if number % 2 == 0:
    parity = "Even"
else:
    parity = "Odd"
print(parity)
# Output: Even

# Short-hand 
number = 10
parity = "Even" if number % 2 == 0 else "Odd"
print(parity) 
# Output: Even






# in c Language 
"""
 if(a>b);

 if(a>b)
 {
 }
"""
i = 1
while i < 6:
  print("rajneesh kumar",end=" ")
  i += 1

  # Python me Increment and Decrement nahi hota hai(i++ && --i ) 

# break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# continue Statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# else Statement in while loop
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")  


# Note: The else block will NOT be executed if the loop is stopped by a break statement.

  


"""
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
"""

day = 4
match day:
  case 1:
    print("Monday")
  case 1:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6.6:
    print("Saturday")
  case "rajneesh":
    print("Sunday")
  case _:
    print("it is default value")   
print("it is out of match body") 



# Combine value
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")


# If Statements as Guards
# You can add if statements in the case evaluation as an extra condition-check: 
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")   
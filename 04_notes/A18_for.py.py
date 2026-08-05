# Loop
# 1) while   Condition based iteration
# 2) for     Iterate for number of elements present     in specified iterable 

# Not Iterable types
#     int, float, complex, bool

# Iterable types
#     str, range, list, tuple, set, dict

# s1="MySirG"
# for e in s1:
#     print(e,ord(e))

s1="abacbdababcdaabc"
count=0
for x in s1:
    if x=='a':
        count+=1
print("count=",count)

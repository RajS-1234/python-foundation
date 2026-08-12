l1 = [10, 20, 30]

# it = iter(l1)

# print(next(it)) # 10
# print(next(it)) # 20
# print(next(it)) # 30

# print(next(it)) 



# How does for loop work?


# numbers = [10, 20, 30]

# for number in numbers:
#     print(number)

# # Python conceptually does something similar to:

# it = iter(numbers)

# while True:
#     try:
#         number = next(it)
#         print(number)
#     except StopIteration:
#         break



    
# class MyIterator:

#     def __init__(self):
#         self.number = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.number <= 3:
#             value = self.number
#             self.number += 1
#             return value

#         raise StopIteration

# it = MyIterator()

# print(next(it))
# print(next(it))
# print(next(it))



class iterator :
    def __init__(self,list) :
        self.list = list
        self.currentPosition=0

    def __next__(self):
        while  self.currentPosition < len(self.list) :
            value = self.list[self.currentPosition]
            self.currentPosition+=1
            return value
        raise StopIteration

it = iterator(l1)  
print(it.list)
print(it.currentPosition)

print(next(it))      
print(next(it))
print(next(it))       
        

    
"""
conceptually:

numbers
   │
   ▼
┌───────────────┐
│ 10 │ 20 │ 30  │
└───────────────┘
  ↑
 position

When we do:

it = iter(numbers)

Python creates an iterator object that maintains its current position.

Initially:

Iterator
   │
   ▼
10  20  30
↑
current position

After:

next(it)

it returns:

10

and moves forward:

10  20  30
    ↑
 current position

Next:

next(it)

returns:

20

and moves:

10  20  30
        ↑

Then:

next(it)

returns:

30


6. What happens after the last element?

Suppose:

numbers = [10, 20, 30]

it = iter(numbers)

next(it)  # 10
next(it)  # 20
next(it)  # 30

Now there is nothing left.

So:

next(it)

raises:

StopIteration

This is how Python knows:

"Iteration is finished."


"""

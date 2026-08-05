# range is a class
# range is a type
# range is an iterable
# range is a sequence
# range object contains an arithmetic Progression (AP)
# range elements are always of type int
# step is by default 1
# single argument is always end value (consider beg=0)
# range object is immutable
# range object has a concept of indexing

# x=range(beg,end,step)
# 1) range(beg,end,step)
# 2) range(beg,end)  # step =1
# 3) range(end) # beg=0, step=1

x=range(2,20,2)

#-9-8-7-6 -5 -4 -3 -2 -1 (negative index)
# 0 1 2 3  4  5  6  7  8  (positive index)
# 2 4 6 8 10 12 14 16 18

i=0
while i<=8:
    print(x[i],end=' ')
    i+=1

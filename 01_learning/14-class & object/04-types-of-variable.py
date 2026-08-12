# """
# Types of variable
# 1) global Variable
# 2) local variable (function object variable)
# 3) Instance Object Variable
# 4) Class Object Variable (static variable)
# """

# #Instance Object Variable
# # instanceObject.variable
# class Test:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def f1(self,c):
#         self.c=c
#         print(self.a,self.b,self.c)

# """ 
# t1=Test(3,4)
# t2=Test(5,6)
# t1.f1(10)
# t2.d=20
# print(t1.__dict__)
# print(t2.__dict__)
# """




# #Class Object Variable | static variable
# #ClassObject.variable

# class Test:
#     x1=10
#     def __init__(self):
#         Test.x2=1
#     def f1(self):
#         Test.x3=2
#     @staticmethod
#     def f2():
#         Test.x4=3
#     @classmethod
#     def f3(cls):
#         Test.x5=4
#         cls.x6=5

# Test.x7=6

# t1=Test()
# t2=Test()
# t1.f1()
# Test.f2()
# Test.f3()
# for k,v in Test.__dict__.items():
#     print(k,v)



s="rajneesh"
wind=""

for right in range(len(s)) :
               wind+=s[right]
if wind == s :
   print(wind)
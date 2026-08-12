"""
#Instance Object variable name conflict
class A:
    def __init__(self):
        self.a=5
class B(A):
    def __init__(self):
        super().__init__()
        self.a=4
        

b1=B()
print(b1.a)
"""

"""
#Class object variable name conflict
class A:
    x=10
class B(A):
    x=20

print(A.x,B.x)
"""

#Instance method name conflict 
"""
#When function name and arguments are same, it is Method Overriding
class A:
    def f1(self):
        print("A")
class B(A):
    def f1(self):
        print("B")

b1=B()
b1.f1()
"""
"""
#When function name is same but arguments are different, it is known as function hiding
class A:
    def f1(self,a):
        print("A")
class B(A):
    def f1(self):
        print("B")

b1=B()
b1.f1() # B
b1.f1(5) #error
"""
"""
#static method name conflict
class A:
    @staticmethod
    def f1(a,b):
        print("A")
    @staticmethod
    def f2(a):
        print("A - f2")
class B(A):
    @staticmethod
    def f1(a,b):
        print("B")
    @staticmethod
    def f2(a,b):
        print("B - f2")
B.f1(3,4)
B.f2(10,20)
"""

class A:
    x=10
    def f1(self,x):
        self.x=20
        print(A.x)
    def f2(self,x):
        self.y=20
        print(self.x)   

a1=A()
a1.f1(3)
a1.f2(5)





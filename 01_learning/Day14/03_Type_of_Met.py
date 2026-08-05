"""
Types of methods 
(consider only those function which are defined in the class body)
1) instance method
2) static method
3) class method

"""

class Test :
        x=10   #class object variable | static variable
        def __init__(self,a,b) : 
               self.a=a
               self.b=b


        def f1(self) : # Instance Method 
               print(self.a,self.b)


        @staticmethod
        def f2(msg) : # Static Method 
              print(msg)
              print("i am static Method")
        
        @classmethod
        def f3(cls) : # Class Method 
              print("i am class Method :")
              cls.x+=1
              print(cls.x)



t1=Test(3,4) # __init__(t1,3,4)
t2=Test(5,6) # __init__(t2,5,6)


"""
#Ways to call instance method
t1.f1() # Test.f1(t1)
t2.f1() # Test.f2(t2)
Test.f1(t1) 
#if we accesing the instance method through the class object 
#then we have to give argument as color object

"""



"""
#ways to call static method 
# No implicit argument
t1.f2("Hello")
t2.f2("Rajneesh")
Test.f2("Kumar") #Preferred

# static Method is not depend on the instance object ,it work on class level
# inka kam class se related function provide karna jo which is same for all the 
# instance object
1. Uses no self and no cls
2.Does not access class or object data
3.just normal fuunction inside the class
"""



#Ways to call class method
t1.f3() # Test.f3(Test)
t2.f3() # Test.f3(Test)
Test.f3() #Test.f3(Test) #Preferred


# for k,v in Test.__dict__.items():
#     print(k,v)


"""
  Important Concept
  class ke kisi v attribute ko ham instance object and class object dot.()
  karge access kar sakte hai
"""
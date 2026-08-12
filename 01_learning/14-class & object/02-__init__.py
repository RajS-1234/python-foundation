class Test :
      # x variable ek bar banega kyu ki class object ka existing ek hi hota hai

      x1=4 # class object variable| static variable 

      # __init__() ka kam hai instance object ke andar member create karna 
      def __init__(self): # minimum ek argument pass karna padhega maximum kitna v pass kar
            self.a=10 # Instance object variable 
            self.b=20 # Instance object variable 
            a=10 # Local variable   when instance object banega to ye local variable destroy ho jayega


      def __init__(self,a,b) :
            self.a=a
            self.b=b


t1=Test() # __init__(t1)
t2=Test() # __init__(t2)

t3=Test(3,4) # __init__(t3,3,4)
t4=Test(5,6) # __init__(t4,5,6)


# init method internal method hai isliye ham isko direct call nahi kar sakte hai
# init method ko call karne ke liye ham class name ke aage ()
#  lagate hai to wo init method ko call kar deta hai

# init method ka kam hai instance object ke andar member variable create karna

"""
Types of variable

1.global
2. local variable(function object variable)
3. insta object variable
4. class object variable | static 

"""




# kisi v obbject le life time me sabse pahle init function call hota hai
# why name self ,a,b
# in c++ Concept this but in python not concept this but self work like this
# ye self us instance object ko repersent karega jo init function ko call kiya hai


l1=[]
l1.append(10)


"""

in c++ color object class private member variable ko access kar sakte hai 

in python we can'nt access direct member variable 
we have to access through self .

class Test
{
      private :
          int a,b;
      public:
          void setdata(int x,int y)
          {
                a=x;
                b=y;
          }
          void setdata(int x,int y)
          {
                a=x;
                b=y;
          }
};
int main() {
               Test t1;
               t1.setdata(10,20)
}


"""
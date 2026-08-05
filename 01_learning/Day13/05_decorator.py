# decorator

# decorators fuunctio 
def cube_decorator(func) :
     def inner(a) :
               print("Before calling cube function")
               func(a)
               print("After calling cube function")
     return inner


 # ye niche wale function ko decorate karega to jo decorator function return karega wo uska place laga
 # jab cube ko call karenge to wo inner function call hoga ,it means jo decorator function return karega wo call hoga
@cube_decorator
def cube(a) :
    print(a*a*a)
cube(5)



print("--------------------------------------------------") 


def Showblance_decorator(fun) :
      def inner() :
            print("Enter Your Password :")
            x=input()
            if(x=='1234') :
                   fun()
            else :
                  print("invalid password ") 
      return inner                   



@Showblance_decorator
def Showbalance() :
      print("Your account balance is 1500")


Showbalance()
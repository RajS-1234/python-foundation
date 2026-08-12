class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name 
    def setAge(self,age):
        self.age=age
    def getAge(self):
        return self.age
class Student(Person):
    
#     def __init__(self, rollnum) : # this function responsibility to create instance member variable of parent object
#         self.rollno = rollnum

#     def __init__(self,rollno, name , age) :
#         self.rollno = rollno
#         self.name = name
#         self.age = age

    def __init__(self,rollno,name,age) :
        self.rollno=rollno
        super().__init__(name,age)
        #Person.__init__(self,name,age)
    def setRollno(self,rno):
        self.rollno=rno
    def getRollno(self):
        return self.rollno
s1=Student(100,"Rajeev",22) 
# Student.__init__(s1,100,"Rajeev",22)
print(s1.getName())
print(s1.getAge())
print(s1.getRollno())
#print(s1.__dict__)

# p1=Person("Harish",31)
# p2=Person("Rajeev",28)
# print("Person 1")
# print("Name: ",p1.getName())
# print("Age: ",p1.getAge())    
# print("Person 2")
# print("Name: ",p2.getName())
# print("Age: ",p2.getAge()) 
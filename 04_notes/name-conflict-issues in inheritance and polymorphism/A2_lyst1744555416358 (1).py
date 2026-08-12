#Polymorphism

"""
class A:
    def f1(self):
        print("A")
class B:
    def f1(self):
        print("B")

obj=A()
obj.f1()
obj=B()
obj.f1()
"""

class Animal:
    def __init__(self,name):
        self.name=name
    def talk(self):
        raise NotImplementedError("Animal not mentioned")
class Dog(Animal):
    def talk(self):
        return "barking..."
class Cat(Animal):
    def talk(self):
        return "meow"

animals=[ 
    Dog("Gabbar"),
    Cat("Rupa"),
    Dog("Tomy"),
    Dog("Bhola"),
    Cat("Sonia"),
    Dog("Mukku")
]

for animal in animals:
    print(animal.name," - ",animal.talk())
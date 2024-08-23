class Person:
# attributes
    Name = "Rashmi"
    Phone = None
    Id = 5001

# behaviour
    def talk(self):
        print("I can talk")
    def walk(self):
        print("I can walk")
#create objects of the person class
ob1=Person() #as soon as this is created a memory is allocated to it
ob1.Name="Anirudh rao" #Can access all attributes and behaviour of the class using this object
ob1.talk()

# I can talk

--------------------------------------------------------------------------------------

class Second:
    def func1(self):
        print("This is no argument no return")
    def func2(self):
        return None
    def func3(self,name):
        print("This is one argument and no return")
    def func4(self,a,b):
        return a+b

ob1=Second()
ob1.func1()
ob1.func2()
ob1.func3("Rashmi")
output1 = ob1.func4(4,5)
print(output1)

# This is no argument no return
# This is one argument and no return
# 9

-------------------------------------------------------------------------------

class Constructor1:
    a= None
    b= None
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("This is called")
        print(a+b)
obj1=Constructor1("Rashmi","Anirudh")
# This is called
# RashmiAnirudh

--------------------------------------------------------------
class Student:
    def __init__(self):
        self.name=input("enter the name: ")
        self.age=input("enter the age: ")
    def display(self):
        print(f"Name is {self.name} and age is {self.age}")

obj1=Student()
obj1.display()
# enter the name: Rashmi
# enter the age: 35
# Name is Rashmi and age is 35
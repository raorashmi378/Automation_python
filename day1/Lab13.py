#---------------------------Single inheritance---------------------------------
class Parent:
    gold = "2kg"

    def BHK2(self):
        print("Parent's 2 BHK")
# class Child(Parent):
    def BHK3(self):
        print("child 3 BHK")

obj=Parent()
child_object=Child()
print(obj.gold)
child_object.BHK3()
child_object.BHK2() #child can access parent's attributes and behaviour

# 2kg
# child 3 BHK
# Parent's 2 BHK

-------------------Hierarchical inheritance----------------------------------------
class Parent:
    def PBHK1(self):
        print("this is parent 1 bhk")
class Child1(Parent):
    def C1BHK1(self):
        print("this is child1 BHK")
class Child2(Parent):
    def C2BHK1(self):
        print("this is child2 BHK")
class Child3(Parent):
    def C3BHK1(self):
        print("this is child3 BHK")
parent1=Parent()
parent1.PBHK1()

child1=Child1()
child1.PBHK1()
child1.C1BHK1()

child2=Child2()
child2.PBHK1()
child2.C2BHK1()

child3=Child3()
child3.PBHK1()
child3.C3BHK1()

# this is parent 1 bhk
# this is parent 1 bhk
# this is child1 BHK
# this is parent 1 bhk
# this is child2 BHK
# this is parent 1 bhk
# this is child3 BHK

----------------------multilevel inheritance-------------------------------------------
class Grandparent:
    def house1(self):
        print("I am house1 of the grandparent")
class Parent(Grandparent):
    def house2(self):
        print("I am house2 of the parent")
class Child(Parent):
    def house3(self):
        print("I am house3 of the child")

g1=Grandparent()
g1.house1()

p1=Parent()
p1.house2()
p1.house1()

c1=Child()
c1.house3()
c1.house1()
c1.house2()

# I am house1 of the grandparent
# I am house2 of the parent
# I am house1 of the grandparent
# I am house3 of the child
# I am house1 of the grandparent
# I am house2 of the parent

-------------------------------multiple level-----------------------------

class Father:
    def money(self):
        return("Getting 5 rupees from father")
class Mother:
    def money(self):
        return("Getting 5 rupees from mother")
class Daughter(Father,Mother):
    def money(self):
        return("Getting 5 rupees from myself")
class Son(Father,Mother):
    pass

f=Father()
print(f.money())

m=Mother()
print(m.money())

d=Daughter()
print(d.money())
print(d.money())

s=Son()
print(s.money())

# Getting 5 rupees from father
# Getting 5 rupees from mother
# Getting 5 rupees from myself
# Getting 5 rupees from myself
# Getting 5 rupees from father

--------------------------------hybrid inheritance------------------------------------

class A:
    def methodA(self):
        print("I am from method A")
class B(A):
    def methodB(self):
        print("I am from method B")
class C(A):
    def methodC(self):
        print("I am from method C")
class D(B,C):
    def methodD(self):
        print("I am from method D")

d=D()
d.methodD()
d.methodA()
d.methodB()
d.methodC()

# I am from method D
# I am from method A
# I am from method B
# I am from method C





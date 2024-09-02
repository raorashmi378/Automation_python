class Multiplereturn:
    def multireturn(self):
        return "99", "Rashmi", False
c=Multiplereturn()
print(c.multireturn())

#('99', 'Rashmi', False)

--------------------------polymorphism--method overriding--------------------------------
class A:
    def shape(self,a,b):
        return a*b
class B:
    def shape(self,a,b):
        return a+b
class C(A,B):
    pass
a=A()
print(a.shape(3,4))

#12
--------------------------------------
class A:
    def sum(self,a,b,c=0):
        return a+b+c
class B(A):
    def sum(self, a,b):
        return a+b
a=A()
print(a.sum(2,3,6))
a.sum(4,5)
#11

-----------------------------------------------------------------------

class A:
    def add(self,a,b):
        return a+b

    def add(self,a,b=0,c=0):
        return a+b+c
a=A()
op1=a.add(1,2)
op2=a.add(1,2,3)
print(op1)
print(op2)

# 3
# 6

---------------------------------------------------------------------

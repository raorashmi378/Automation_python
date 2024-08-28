# class Person:
#     name = "Promod"
#     age= None
#
#     def func1(self):
#         a=10
#         print("I am a method")
#         print("My age is", self.age)
#
# obj1=Person()
# obj1.func1()
# #I am a method
# #My age is None

#----------------------------------------------------------------------------

# class Car:
#     name:None
#     model:None
#     brand:None
#     Year: None
#
#     def method1(self,oname,omodel,obrand,oyear):
#         self.name=oname
#         self.model=omodel
#         self.brand=obrand
#         self.year=oyear
#
#     def display(self):
#         print("the name of the car is:",self.name)
#         print("the model of the car is:", self.model)
#         print("the brand of the car is:", self.brand)
#         print("the year of the car is:", self.year)
#
# obj1=Car()
# obj1.method1("Ignis","v2","Maruthi",2017)
# obj1.display()
# # the name of the car is: Ignis
# # the model of the car is: v2
# # the brand of the car is: Maruthi
# # the year of the car is: 2017

#-------------------------------Encapsulation----------------------------------------------

# class Encapsulation1:
#     def publicmethod(self,name,email):
#         self.name=name
#         self.email=email
#         print("I am a public method")
#
#     def _protectedmethod(self):
#         print("I am a protected method")
#
#     def __privatemethod(self):
#         print("I am a private method")
#
# obj1=Encapsulation1()
# obj1.publicmethod("Rashmi","ras@gmail.com")
#
# #I am a public method

#------------------------calling private method-----------------------------------
#

#class Encapsulation1:
#     def publicmethod(self,name,email):
#         self.name=name
#         self.email=email
#         print("I am a public method")
#         self.__privatemethod()
#
#     def _protectedmethod(self):
#         print("I am a protected method")
#
#     def __privatemethod(self):
#         print("I am a private method")
#
# obj1=Encapsulation1()
# obj1.publicmethod("Rashmi","ras@gmail.com")
#
# #I am a public method
# #I am a private method

#--------------------------------------------------------
# class Myclass:
#     def __init__(self):
#         self.name="Rashmi"
#     def publicmethod(self):
#         print("I am public")
#         self.__private_method()
#     def __private_method(self):
#         print("I am a private method")
#
# obj=Myclass()
# obj.publicmethod()
# # I am public
# # I am a private method

#--------------------------------------------------------------------
# class VMOlogin:
#     def __init__(self,email,password):
#         self.__email=email
#         self.__password=password
#
#     def loginconfirm(self):
#         if self.__email=="ras@gmail.com" and self.__password=="pass123":
#             print("allowed")
#         else:
#             print("not allowed")
#
# obj1=VMOlogin("ras@gmail.com","pass123")
# obj1.loginconfirm()
#
# #allowed

#---------------------------------------------------------------
# class Bankaccount:
#     def __init__(self):
#         self.balance = 0
#         self.__privatevariable = 100
#
#     def pubmethod(self):
#         print(self.__privatevariable)
#
#     def deposit(self,amount):
#         self.balance = self.balance+amount
#     def withdraw(self,amount):
#         self.balance=self.balance-amount
#     def showbalance(self):
#         print("your balance is: ", self.balance)
# obj1=Bankaccount()
# obj1.deposit(100)
# obj1.showbalance()
# obj1.withdraw(99)
# obj1.showbalance()
#
# #your balance is:  100
# #your balance is:  1

#------------using encapsulation for the above code-----------------------
# class Bankaccount:
#     def __init__(self):
#         self.balance = 0
#         self.__privatevariable = 100
#
#     def pubmethod(self):
#         print(self.__privatevariable)
#
#     def deposit(self,amount):
#         self.balance = self.balance+amount
#     def __withdraw(self,amount):
#         self.balance=self.balance-amount
#     def __showbalance(self):
#         print("your balance is: ", self.balance)
#     def aunthenticated(self,flag):
#         if flag:
#             self.__showbalance()
#         else:
#             print("not allowed")
#     def authWithdraw(self,auth,amount):
#
#         if auth:
#             self.__withdraw(amount=amount)
#         else:
#             print("not allowed")
# obj1=Bankaccount()
# obj1.deposit(100)
# obj1.aunthenticated(True)
# # your balance is:  100
# # your balance is:  1
# # your balance is:  100
#---------------------------------------------------------------------
class Login:
    def __init__(self,password):
        self.__password=password

    def get_pwd(self,auth):
        if auth:
            print(self.__password)
        else:
            print("invalid password")
    def set_pwd(self, password):
        if len(password)>5:
            self.__passowrd = "password1"
        else:
            print("not allowed")


obj=Login("password123")
obj.get_pwd(True)
obj.set_pwd("pwd123")
#password123



print("hello", "123", "2.42", "one")
#hello 123 2.42 one
#by default seperator is space

print("hello", "123", "2.42", "one",sep="-")
#hello-123-2.42-one

print("Hi, I am Rashmi Rao", "How are you doing?")
#Hi, I am Rashmi Rao How are you doing?

print("Hi, I am Rashmi Rao", "How are you doing?",end="")
print("What else")
#Hi, I am Rashmi Rao How are you doing?What else
#By default end is \n meaning next line

print("Hi, I am Rashmi Rao", "How are you doing?")
print("What else")
#Hi, I am Rashmi Rao How are you doing?
#What else

#-------------------------max function----------------------------------------------------
#program to find max of 2 numbers
print(max(20,30,88,100.84,-1,0,-20.85))
#100.84

print(max(20,30,88))
#TypeError: '>' not supported between instances of 'str' and 'float'

#------------------------Data types----------------------------------------------------------
age=30
print(type(age))
#<class 'int'>

num=3.14
print(type(num))
#<class 'float'>

val=True
print(type(val))
#<class 'bool'>

import keyword
print(keyword.kwlist)
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#--------------------------taking input from user----------------------------------------------------------
variable1 = input("enter your name")
print("your name is:", variable1)
#enter your name(user will type here) rashmi
#your name is: rashmi







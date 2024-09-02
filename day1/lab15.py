##-------------------exception handling--------------------------------
try:
    a = int(input("enter the first number: "))
    b= int(input("enter the second number: "))
    c=a/b
    print("Result is", c)
except:
    print("please enter valid input")
# enter the first number: 10
# enter the second number: 0
# please enter valid input

##-----------------errors----------------------
 print("I am Rashmi") #IndentationError: unexpected indent
result = 5 + "5" #TypeError: unsupported operand type(s) for +: 'int' and 'str'
int("rashmi") #ValueError: invalid literal for int() with base 10: 'rashmi'
print(undefined_variable) #NameError: name 'undefined_variable' is not defined

mylist=[1,2,3]
print(mylist[3]) #IndexError: list index out of range

mydict = {'a':1,"b":2}
print(mydict["c"]) #KeyError: 'c'

result=10/0 #ZeroDivisionError: division by zero

import nonexistingmodule  #ModuleNotFoundError: No module named 'nonexistingmodule'

while True print("I am right") #SyntaxError: invalid syntax

##-------------------------------------------------------------------------------------
try:
    a= int(input("enter the number1: "))
    b= int(input("enter the number2: "))
    c=a/b
    print(c)
except ValueError as ve:
    print(ve)
except ZeroDivisionError as ze:
    print(ze)
finally:
    print("I will be executed anyhow")

# enter the number1: 10
# enter the number2: 2
# 5.0
# I will be executed anyhow

# enter the number1: 10
# enter the number2: 0
# division by zero
# I will be executed anyhow

# enter the number1: a
# invalid literal for int() with base 10: 'a'
# I will be executed anyhow
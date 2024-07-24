for i in range(11):
    print("hello world")
# hello world
# hello world
# hello world
# hello world
# hello world
# hello world
# hello world
# hello world
# hello world
# hello world
# hello world

for i in range(1, 10, 2):
    print(i)
# 1
# 3
# 5
# 7
# 9

i=0
while i<5:
    print(i)
    i=i+1
# 0
# 1
# 2
# 3
# 4

# TASK1
##write a program which gives grades based on the score entered

num = int(input("enter the score: " ))
if 90<=num<=100:
    print("A")
elif 80<=num<=89:
    print("B")
elif 70<=num<=79:
    print("C")
elif 60<=num<=69:
    print("D")
elif 0<=num<=59:
    print("F")
else:
    print("invalid score")
# enter the score: 60
# D

# TASK2
# Create a program that determines whether a given year is a leap year
year = int(input("enter the year: "))
if (year%4==0 or year%400==0):
    print("It is a leap year")
else:
    print("It is not a leap year")
# enter the year: 2004
# It is a leap year
# enter the year: 2005
# It is not a leap year

#type of triangle based on the sides
side1 = float(input("enter the side1: "))
side2 = float(input("enter the side2: "))
side3 = float(input("enter the side3: "))
if side1==side2==side3:
    print("It is a equilateral triangle")
elif side1==side2 or side1==side3 or side2==side3:
    print("It is an isoscles triange")
elif side1!=side2!=side3:
    print("It is a scalene triangle")
else:
    print("Type is not defined")
# enter the side1: 30
# enter the side2: 10
# enter the side3: 30
# It is an isoscles triange

# Factorial of a number
num = int(input("enter the number: "))
i=1
res=1
while num>=i:
    res=res*i
    i=i+1
print(res)
# enter the number: 6
# 720

# write a program to print even and odd numbers
for even in range(0,10,2):
    print(even)
# 0
# 2
# 4
# 6
# 8
for odd in range(1,10,2):
    print(odd)
# 1
# 3
# 5
# 7
# 9

for br in range(0,20):
    print(br)
    if br==5:
        break
print("just broke")
# 0
# 1
# 2
# 3
# 4
# 5
# just broke

for ps in range(6):
    if ps==3:
        pass
    else:
        print(ps)
# 0
# 1
# 2
# 4
# 5

#Using match for multiple conditions
num = int(input("enter a number: "))
match num:
    case 1:
        print("you have entered number 1")
    case 2:
        print("you have entered number 2")
    case _:
        print("No idea")
#enter a number: 3
#No idea
# enter a number: 2
# you have entered number 2

def greet():
    print("wassup dude")
#No output in this case as the function is just defined and not called

def greet():
    print("wassup dude")
greet()
#wassup dude

def greet():
    print("wassup dude")
greet()
greet()
greet()
greet()
# wassup dude
# wassup dude
# wassup dude
# wassup dude

#functions with arguments
def greet(name):
    print("Hi, how are you", name)
greet("Rashmi")
greet("Anirudh")
greet(123)
#Hi, how are you Rashmi
# Hi, how are you Anirudh
# Hi, how are you 123
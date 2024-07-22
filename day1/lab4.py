#calculate the area of the circle
import math
r = int(input("enter the number: "))
print(math.pi * r**2)
#enter the number: 3
#28.274333882308138

#calculate the square of the number
r = float(input("enter the number: "))
square = r**2
print(square)
#enter the number: 3
#9.0

#calculate the cube of a number
r = float(input("enter the number: "))
cube = r**3
print(cube)
#enter the number: 4
#64.0


#ternary operator
#take 2 inputs from the user and check first number is greater than, less than or equal to the second number
firstnum = float(input("enter the first number: " ))
secondnum = float(input("enter the second number: "))
print("first number is greater" if(firstnum>secondnum) else "Second number is greater")
print("first number is equal to second" if(firstnum==secondnum) else "first number is not equal to second number")
#enter the first number: 10
#enter the second number: 10
#first number is equal to second


#filter
num = [1,2,3,4,5,6,7,8,9,10]
def func1(arg1):
    return arg1 % 2 == 0

output=filter(func1,num)
print(output)
#<filter object at 0x000001D1E9B13A30>

print(list(output))
#[2, 4, 6, 8, 10]
------------------------------------------------------------
#get only vowels
list1=['q','w','e','a','i','o','U','r','s','t']
def func2(arg1):
    return arg1 in 'aeiouAEIOU'

output = filter(func2,list1)
print(list(output))
#['e', 'a', 'i', 'o', 'u']

-------------------------------------------------------------------------

#recursive program for factorial
def fact1(arg1):
    #base case
    if arg1==0:
        return 1
    #recursive case
    else:
        return arg1*fact1(arg1-1)

print(fact1(5))
#120

------------------------------------------------------------------
#leet code --sum of the digits
rem1=12345%10
print(rem1)
quotient = 12345//10
print(quotient)
#5
#1234


def sum_digits(arg1):
    sum_digits=0
    while arg1>0:
        sum_digits=sum_digits+ arg1%10
        arg1=arg1//10
    return sum_digits
print(sum_digits(12345))
#15
----------------------------------------------------------
#pattern program

for i in range(0,6):
    for j in range(1,6):
        if j<=i:
            print(" ", end=" ")
        else:
            print("*", end=" ") #end is given so that it does not go to the ne line
    print()  #after every row a new line is added
# # * * * * *
# #   * * * *
# #     * * *
# #       * *
# #         *
------------------------------------------------------------------




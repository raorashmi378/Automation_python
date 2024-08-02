global_variable = 6
def f1():
    print(global_variable)
f1()
#6

global_variable = 6
def f1():
    local_variable = 9
    print(local_variable)
    print(global_variable)
f1()
#9
#6

global_variable = 6
def f1():
    local_variable = 9
    print(local_variable)
    print(global_variable)
f1()
print(global_variable)
print(local_variable)
#9
#6
#6
#NameError: local_variable is not defined

numbers=[1,2,3]
def f3(numbers):
    numbers[0] = 100
    return numbers
l= f3(numbers)
print(l)
#[100, 2, 3]


numbers=[1,2,3]
def f4(num):
    numbers[0]=100
l1=f4(numbers)
print(l1)
#None

def outer_f1():
    print("this is outer")
    def inner_f2():
        print("this is inner")
    inner_f2()

outer_f1()
#this is outer
#this is inner

numbers=[1,2,3]
def f1(var1):
    numbers.append(100)
    print(numbers)
def f2(var2):
    numbers[2]=4
    print(numbers)
numbers.append(110)
print(numbers)
#[1, 2, 3, 110]

numbers=[1,2,3]
def f1(var1):
    numbers.append(100)
    print(numbers)
def f2(var2):
    numbers[2]=4
    print(numbers)
numbers.append(110)
print(numbers)
f1(numbers)
f2(numbers)
#[1, 2, 3, 110]
#[1, 2, 3, 110, 100]
#[1, 2, 4, 110, 100]

lambda

def f1(var1):
    return var1 * 2
l=f1(100)
print(l)
#200

l = lambda var1:var1*2
print(l(100))
#200

output=lambda num:"even" if num%2==0 else "odd"
print(output(10))
#even
--------------------------------------------------------------
double the numbers
list1=[1,2,3,4]
temp_list=[]
for i in list1:
    list2=[i*2]
    temp_list=temp_list+list2
print(temp_list)
#[2, 4, 6, 8]

#Same code is executed using map() function below
list1 =[1,2,3,4]
def f1(num):
    return num*2
output= list(map(f1,list1))
print(output)
#[2, 4, 6, 8]

#Same code is executed without using map() function below
list1 =[1,2,3,4]
def f1(num):
    return num*2
output=f1(list1)
print(output)
#[1, 2, 3, 4, 1, 2, 3, 4]

list1 =[1,2,3,4]
f1=lambda num:num*2
output= list(map(f1,list1))
print(output)
#[2, 4, 6, 8]

































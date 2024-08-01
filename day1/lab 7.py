def f1():
    print("hello")
f1()
#hello

def f1():
    print("hello")
result = f1()
print(result)
#hello
#None

def f1(name="Rashmi"):
    print(name)
f1("Deeksha")
f1("Rohit")
#Deeksha
#Rohit

def adds(a, b):
    return a + b
result = adds(4, 5)
print(result)
#9

def adds(a, b):
    return a + b
    print("this will not be printed as it is after return")
result = adds(4, 5)
print(result)
print("end")
#9
#end

def arguments1(*args):
    for i in args:
        print(i)
arguments1("Rashmi","Anirudh", "Nikhil")
#Rashmi
#Anirudh
#Nikhil

def pizza(*toppings):
    for i in toppings:
        print(i,sep="")
pizza("Tomato")
pizza("orange","pineapple","mushroom")
#Tomato
#orange
#pineapple
#mushroom
def pizza2(*toppings, base):
    print(toppings, base)
pizza2("orange","curds", base="thin crest")
#('orange', 'curds') thin crest


factorial =1
n=int(input("enter the number: "))
for i in range(1, n+1):
    factorial = factorial*i
print(factorial)
#enter the number: 4
#24


# #Take 2 numbers from the user and add them
num1 = int(input("enter the number: "))
num2 = int(input("enter the number: "))
result = num1+num2
print(result)
# #enter the number: 10
# #enter the number: 20
# #30

dir = r'https://docs.google.com/'  #raw string
print(dir)
# #https://docs.google.com/

first_name = "rashmi"
last_name = "rao"
print(first_name, last_name)
print(f'my name is {first_name} {last_name}')
# #rashmi rao
# #my name is rashmi rao

num = 5
print(f"{num} x 1 = {num}")
print(f"{num} x 2 = {num*2}")
print(f"{num} x 3 = {num*3}")
print(f"{num} x 4 = {num*4}")
print(f"{num} x 5 = {num*5}")
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15
#5 x 4 = 20
#5 x 5 = 25



name = "Amithaa"
print(len(name)) #7
print(type(name)) #string
print(name[0])  #A
print(name.count("a"))  #2
name[2] = "o"
print(name[2]) # TypeError: 'str' object does not support item assignment. String is immutable

val = "this is a biggest line"
print(len(val)) #22
print(val[-1])  #e
print(val[-6])  #t
print(val[6])   #s

a= None
print(a) #None
print(type(None)) #NoneType

l1 = ["bread", "butter", "milk", "paneer", "poha"] #homogenous list
print(type(l1))  #list
print(l1[4])   #poha

#l1 = ["bread", "butter", 10, "paneer", 4.87] #heterogenous list
# print(type(l1))  #list
# print(l1[4])   #4.87
# print(len(l1)) #5

# l1[0] = "soya"
# print(l1) # ['soya', 'butter', 10, 'paneer', 4.87] #mutuable
#
#---------built in functions of list-----------------------------------------
# l1.append("curd")
# print(l1)   #['soya', 'butter', 10, 'paneer', 4.87, 'curd']
#
# l1.insert(2,"jam")
# print(l1) #['soya', 'butter', 'jam', 10, 'paneer', 4.87, 'curd']
#
# l1.extend(["pathrado","sannapolo"])
# print(l1)   #['soya', 'butter', 'jam', 10, 'paneer', 4.87, 'curd', 'pathrado', 'sannapolo']

l1= ['soya', 'butter', 'jam', 10, 'paneer', 4.87, 'curd', 'pathrado', 'sannapolo']

# l1.remove("butter")
# print(l1) #['soya', 'jam', 10, 'paneer', 4.87, 'curd', 'pathrado', 'sannapolo']

print(l1.index("jam"))
#2

l1.clear()
print(l1)
#[]

l2 = ["rashmi", "raghuveer"]
l2.copy()
print(l2)
#['rashmi', 'raghuveer']

print(dir(list()))
#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
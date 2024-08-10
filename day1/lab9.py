t=(1,2,3)
list1=list(t)
print(list1)
# #[1, 2, 3]

t1=tuple([1,2,3])
print(t1)
#(1, 2, 3)


countries = ("Japan","Tokyo")
print(countries[1])
#Tokyo
countries1 = (("Denmark","Diu"),("India", "Pakistan"))
print(countries1[0])
#('Denmark', 'Diu')
print(countries1[0][1])
#Diu
countries2 = (("Japan","Diu"),("Dubai","Bangalore","Telangana"),("Czech Republic","Singapore","Denmark"))
print(countries2[1][2])
#Telangana
countries3 = (((("Abu dabi","finland","France","Italy"))))
print(countries3[1])
#finland

set1 = {1,2,3,4,5}
set2 = {4,5,8,9,10}
result = set1.difference(set2)
print(result)
#{1, 2, 3}

def complete_in_future():
    pass
complete_in_future()
#empty like no output

def my_decorator(func):
    def wrapper():
        print("starting----------")
        func()
        print("ending---------------")
    return wrapper()
@my_decorator
def f1():
    print("hello")
#starting----------
#hello
#ending---------------

dict1= {
    "name":"Rashmi",
    "age":34,
    "place":"Bengaluru",
    "area":"Ramurthy Nagar"
}
print(len(dict1))
#2

dict1["name"] = "Suresh"
print(dict1)
#{'name': 'Suresh', 'age': 34}

print(dict1["area"])
#Ramurthy Nagar

print(dict1.get("area"))
#Ramurthy Nagar

print(dict1.values())
#dict_values(['Suresh', 34, 'Bengaluru', 'Ramurthy Nagar'])

print(dict1.keys())
#dict_keys(['name', 'age', 'place', 'area'])

for m,n in dict1.items():
    print(m,n)
# name Suresh
# age 34
# place Bengaluru
# area Ramurthy Nagar
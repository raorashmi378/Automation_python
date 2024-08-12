#print a right triangle for n=5 of * ** *** **** ***** ****** lines

symbol =""
for i in range(0,6):
    symbol= symbol+"*"
    print(symbol)
# *
# **
# ***
# ****
# *****
# ******
-----------------------------------------------------------------------------------
#palindrome of a string NAMAN, nitin, level, rashmi

name = input("enter the name: ")
name1=name[::-1]   #reversing a string using indexing
if name==name1:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
# enter the name: naman
# It is a palindrome
-----------------------------------------------------------------------------------------------

#give the duplicate in a string
string1= input("enter the string: ")
dups=[]
for i in string1:
    if string1.count(i)>1 and i not in dups:
        dups.append(i)
print(dups)
#['a', 'l']

------------------------------------------------------------------------------------

#count the vowels and consonants in a string

string1 = input("Type the string: ")
vowels1 = 0
consonants = 0
for i in string1:
    if i in "aeiouAEIOU":
        vowels1= vowels1+1
    else:
        consonants = consonants +1
print("the number of vowels are:", vowels1)
print("the number of consonants are:", consonants)
# Type the string: rashmi
# the number of vowels are: 2
# the number of consonants are: 4
----------------------------------------------------------------------------------------


#anagram silent and listen, length and letters should be same, nitin and promod are not anagrams
string1=input("enter the first string: ")
string2=input("enter the second string: ")
res1=sorted(string1)
res2=sorted(string2)
print(res1)
if res1==res2:
    print("it is a anagram")
else:
    print("it is not an anagram")

# enter the first string: listens
# enter the second string: silent
# ['e', 'i', 'l', 'n', 's', 's', 't']
# it is not an anagram
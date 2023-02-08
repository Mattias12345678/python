"""
#1
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) / int(num2)

print(result)
result2 = int(num1) % int(num2)
print("You got " + (str(result2)) + " as a rest")
print("Vi fick in " + (num1) + " och " + (num2) + " as input")

#2
import math
num3 = int(input("Enter a number"))
num4 = float(input("Enter another number"))
x = float(num3)
y = int(num4)
print(x)
print(y)

#3
from math import*
num1 = input(" ")
num2 = input(" ")
print(())

#4
def numbers(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        print("The smallest one is" + str(num1))
    elif num2 <= num1 and num2 <= num3:
        print("The smallest one is" + str(num2))
    else:
        print("The smallest one is" + str(num3))

    num1 = 7
    num2 = 6
    num3 = 5

def number(numb1, numb2, numb3):
    if numb1 < numb2 and numb3:
        return numb1
    if numb2 < numb3 and numb1:
        return numb2
    if numb3 < numb1 and numb2:
        return numb3
nu1 = input("skriv en number:")
nu2 = input("skriv en till:")
nu3 = input("skriv en sista")
print(number(nu1, nu2, nu3))

#5
list1 = ["Kevin" , "Karen" , "Jim" , "Timmy" , "Jeff"]
list2 = list1.copy()
list2.reverse()
element1 = list2[0]
list1.insert(2, element1)


print(list1.count(element1))
print(list1)
print(list2)

words1 = ["1" , "2" , "3" , "4" , "5"]
words1.append(6)
words1.extend("67")

print(words1)

#6
a = input("täljare 1")
b = input("nämnare 1")
c = input("täljare 2")
d = input("nämnare 2")
e = input("täljare 3")
f = input("nämnare 3")

a1 = (float(a)+float(d))
b1 = (float(b)+float(d))
c1 = (float(c)+float(b))
d1 = (float(d)+float(b))
e1 = (float(e)+float(d1))
f1 = (float(f)+float(d1))
a2 = (float(a1)+float(f))
c2 = (float(c1)+float(f))
ans = float(a2)+float(c2)+float(e1)
ans2 = math.gcd("3/6")

#7
a = input("what is ur first name")
b = input("what is ur last name")
print(a[:4],b[-3:])
"""



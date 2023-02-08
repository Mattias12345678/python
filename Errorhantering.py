# Errorhantering
#1)
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)

    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)

#2)
name = input("name: ")
age = int(input("age: "))

try:
    print(name + age)

except TypeError:
    print(name + str(age))

print(name+age)

#3)

try:
    numerator = int(input("Write a number above zero: "))
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0")
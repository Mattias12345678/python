"""
#Uppgift 1.2
a = 10
b = 9
c = 8

variabel1 = a, b, c
alpha = True

variabel2 = a
variabel3 = 1
variabel4 = b
variable15 = alpha

print(variabel1)
print(variabel2)
print(variabel3)
print(variabel4)
print(variablel5)

#Uppgift 1.3
print(1/3)
print('1/3')
a = 1/3
print(a)
print('a')

#Uppgift 1.4
person1Age = 16
person1Height = 184
person1Utbildning = True
person2Age = 16
person2Height = 185
person2Utbildning = True
person3Age = 17
person3Height = 190
person3Utbildning = True

print("Person1 is " + str(person1Age) + " and is " + str(person1Height) + ". Has the person gone to school?" + str(person1Utbildning))
print("Person2 is " + str(person2Age) + " and is " + str(person2Height) + ". Has the person gone to school?" + str(person2Utbildning))
print("Person3 is " + str(person3Age) + " and is " + str(person3Height) + ". Has the person gone to school?" + str(person3Utbildning))

#Uppgift 3.1

def adderaTreTal(a, b, c):
    z = (a + b + c)
    return z

a = int(input("Write a number: "))
b = int(input("Write anohter number: "))
c = int(input("Write yet another number: "))

print(adderaTreTal(a, b, c))


#Uppgift 3.2

def calculator():
    while True:
        print("Enter '+' for addition")
        print("Enter '-' for subtraction")
        print("Enter '*' for multiplication")
        print("Enter '/' for division")
        print("Enter 'q' to quit")
        operator = input("Enter operator: ")

        if operator == 'q':
            break
        elif operator in ['+', '-', '*', '/']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if operator == '+':
                print(num1 + num2)
            elif operator == '-':
                print(num1 - num2)
            elif operator == '*':
                print(num1 * num2)
            elif operator == '/':
                if num2 == 0:
                    print("Cannot divide by zero")
                else:
                    print(num1 / num2)
        else:
            print("Invalid operator")
calculator()

#7
elever = ['Axel', 'Johan', 'Johanna', 'Oscar', 'Bill']
elever.sort()
print(elever)

elever = ['Axel', 'Johan', 'Johanna', 'Oscar', 'Bill']
for i in elever:
    print(i)

elever = ['Axel', 'Johan', 'Johanna', 'Oscar', 'Bill']
elever.append("Mattias")
elever.append("Bebe")
elever.sort()
print(elever)

elever = ['Axel', 'Johan', 'Johanna', 'Oscar', 'Bill']

if len(elever):
    print("list is not empty")

else:
    print("list is empty")

elever = ['Axel', 'Johan', 'Johanna', 'Oscar', 'Bill']
new_list = elever.copy()
print(new_list)

elever = ['Axel', 'Johan', 'Johanna', 'Oscar', 'Bill']
basgrupp1 = elever[0:3]
basgrupp2 = elever[3:5]
print(basgrupp1)
print(basgrupp2)

nummer = [1, 3, 4, 6, 2, 5]
nummer.sort()
print(nummer)
nummer.reverse()
print(nummer)
"""









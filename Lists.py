
#1
friends = ["Kevin" , "Karen" , "Jim"]
print(friends[1])
print(friends[0])
print(friends[2])
print(friends[-1])
print(friends[-2])

people = ["Kevin" , "Karen" , "Jim" , "Oscar" , "Tim"]
people[1] = "Mike"
print(friends[1])

#2
def sortedList(t1, t2, t3):
    l2 = [] #detta kommer vara listan som fylls med tal
    if t1<=t2 and t1<=t3:
        l2.append(t1)
        if t2<=t3


list1 = [tal1, tal2, tal3]
print(list1)

list2 = sortedList(tal1, tal2, tal3)
list3 = []
for element in list1:
    list3.append(element)
for element in list2:
    list3.append(element)

for element in list3:
    print(str(element)) + "+" )

#3
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")

print(friends)
print(friends.index("Oscar"))
print(friends.index("Kevin"))

People = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
cars = ["Ford, Volvo"]

print(People)
print(cars)








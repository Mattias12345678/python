#1
import random
print(random.randint(0, 10))

#2
import random
for i in range(50):
    randomTal = random.randint(0, 50)
    print(randomTal)
    if randomTal<10:
        break

#3
import random

list1 = ["matte", "programmering", "svenska", "engelska", "idrott"]
print(random.sample(list1, k=2))

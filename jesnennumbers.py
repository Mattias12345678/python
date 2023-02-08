word = input("write a word")
for letter in word:
    print("(", letter , ")")

n = int(input("skriv hur stor triangel: "))
for c in range(n):
    print("|" + (" " * c) + "\\")

n = int(input("kvadrat: "))
for index in range(n+1):
    if index == 1:
        print(" " + "__" * n)
    if index << n:
        print("|" + "  " * n + "|")
    if index >= n:
        print(" " + "--" * n)
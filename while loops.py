#1
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")

# 2 + guessing game

secret_word = "moneky"
guess = ""
guess_count = 0
guess_limit = 3
out_off_guesses = False

while guess != secret_word and not (out_off_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_off_guesses = True

if out_off_guesses:
    print("Out of guesses, you lose")
else:
    print("You win!")

#3
i = 2
while i <= 20:
    print(i)
    i += 2

#4
tak = 100
summa = 0

while summa <= 100:
    n = int(input("skriv ett tal: "))
    summa += n
    print("Summa är" + str(summa) + ".")

print("över 100")

#5
summa = int(input("skriv ett tal"))
while summa > 100:
    print("ditt tal är större än 100")
if summa < 100:
    print("ditt tal är mindre än 100")

#5
svar = "nej"
svar2 = "ja"
guess = ""

print("Vill du spela ett spel? ")
input("Enter a guess: ")
while guess != svar:
    guess = input("Vill du spela igen? ")
    if guess == svar:
        guess = input("Är du säker: ")
        if guess == svar2:
            guess = input("Jag vill inte spela med dig")

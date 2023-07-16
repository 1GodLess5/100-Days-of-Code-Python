import random
import library

print("Welcome to the PyPassword Generator!")
lettersNumber = int(input("How many letters would you like in your password?\t"))
symbolsNumber = int(input(f"How many symbols would you like?\t"))
numbersNumber = int(input(f"How many numbers would you like?\t"))

password = []
charactersSum = lettersNumber + symbolsNumber + numbersNumber

for i in range(lettersNumber + 1):
    password.append(library.listLetters[random.randint(0, len(library.listLetters) - 1)])
for i in range(numbersNumber + 1):
    password.append(library.listNumbers[random.randint(0, len(library.listNumbers) - 1)])
for i in range(symbolsNumber + 1):
    password.append(library.listSymbols[random.randint(0, len(library.listSymbols) - 1)])

random.shuffle(password)

finalPassword = ""
for i in range(charactersSum):
    finalPassword += password[i]

print(finalPassword)

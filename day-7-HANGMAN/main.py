import random
import os
import design

wordsList = []
display = []

wordsFile = open("wordsList.txt", "r")
for word in wordsFile:
    wordsList.append(word.strip("\n"))
wordsFile.close()

fileLength = len(wordsList)
chosenWord = wordsList[random.randint(0, fileLength - 1)]

for letter in chosenWord:
    display.append("_")
print(display)

# cheating
print(chosenWord)

exitHangman = False
wrongGuessCounter = 0

# main loop
while not exitHangman:
    displayCounter = 0
    userGuess = input("Guess a letter:\t").lower()

    for letter in chosenWord:
        if userGuess == letter:
            display[displayCounter] = letter
        else:
            pass
        displayCounter += 1

    print(display)

    if ''.join(display) == chosenWord:
        os.system("clear")
        print(design.color.BOLD + design.color.GREEN)
        print("You guessed the correct word " + ''.join(display).upper() + " !")
        print("YOU WIN!")
        print(design.color.END)
        exitHangman = True























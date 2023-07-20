import random
import os
import time
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

lives = 6

# main loop
while not exitHangman:
    displayCounter = 0
    wrongGuessCounter = 0
    userGuess = input("Guess a letter:\t").lower()

    for letter in chosenWord:
        if userGuess == letter:
            display[displayCounter] = letter
        else:
            wrongGuessCounter += 1
        displayCounter += 1
    print(display)

    if wrongGuessCounter == len(chosenWord):
        lives -= 1
        print(f"Lives left: {lives}")
        print(design.stages[lives])
    print("\n\n")

    if ''.join(display) == chosenWord:
        time.sleep(3)
        os.system("clear")

        print(design.color.BOLD + design.color.GREEN)
        print(f"You guessed the correct word: {chosenWord.upper()} !")
        print("YOU WIN!")
        print(design.color.END)

        exitHangman = True

    elif lives == 0:
        time.sleep(5)
        os.system("clear")

        print(design.stages[0])
        print(design.color.BOLD + design.color.RED)
        print(f"The correct word was: {chosenWord.upper()} !")
        print("YOU LOOSE!")
        print(design.color.END)

        exitHangman = True























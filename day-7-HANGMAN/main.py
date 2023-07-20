import random
import os
import time
import design
from pynput import keyboard

# initial variables
wordsList = []
display = []
exitHangman = False
lives = 6
wrongLetters = []

# opening wordsList.txt file
wordsFile = open("wordsList.txt", "r")
for word in wordsFile:
    wordsList.append(word.strip("\n"))
wordsFile.close()

# gets random word from file
fileLength = len(wordsList)
chosenWord = wordsList[random.randint(0, fileLength - 1)]

# initial ascii
print(design.hangmanArt)
input("Press any key to continue. ")
keyboard.Events()
os.system("clear")

# start of the game
for letter in chosenWord:
    display.append("_")
print(display)

# cheating
#print(chosenWord)

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

    # checking if users guess was correct and printing out
    if wrongGuessCounter == len(chosenWord):
        lives -= 1
        wrongLetters.append(userGuess)
        print(f"Lives left: {lives}")
        print(design.stages[lives])
    print(f"Wrong guesses: {', '.join(wrongLetters)}")
    print("\n")

    # decides if user won or not
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


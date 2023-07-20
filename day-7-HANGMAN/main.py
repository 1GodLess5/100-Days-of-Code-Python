import random

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
            print("Nope")
        displayCounter += 1

    print(display)






















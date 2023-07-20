import random

wordsList = []

wordsFile = open("wordsList.txt", "r")
for word in wordsFile:
    wordsList.append(word.strip("\n"))
wordsFile.close()

fileLength = len(wordsList)
chosenWord = wordsList[random.randint(0, fileLength - 1)]

# cheating
print(chosenWord)

exitHangman = False

while not exitHangman:
    userGuess = input("Guess a letter:\t").lower()

    for letter in chosenWord:
        if userGuess == letter:
            print("Yup")
        else:
            print("Nope")


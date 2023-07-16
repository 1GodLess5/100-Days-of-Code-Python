def listFill(start: int, end: int):
    list = []
    for i in range(start, end +1):
        list.append(i)

    return list

def asciiConverter(listOfNumbers: list):
    counter = 0
    newAscii = ""

    for number in listOfNumbers:
        listOfNumbers[counter] = chr(number)
        counter += 1

    return listOfNumbers


# ASCII for symbols -> 33 - 47; 58 - 64; 91 - 96
listSymbols = []
listSymbols.extend(listFill(33, 47))
listSymbols.extend(listFill(58, 64))
listSymbols.extend(listFill(91, 96))
listSymbols = asciiConverter(listSymbols)

# ASCII for numbers -> 48 - 57
listNumbers = []
listNumbers.extend(listFill(48, 57))
listNumbers = asciiConverter(listNumbers)

# ASCII for letters -> 65 - 90; 97 - 122
listLetters = []
listLetters.extend(listFill(65, 90))
listLetters.extend(listFill(97, 122))
listLetters = asciiConverter(listLetters)

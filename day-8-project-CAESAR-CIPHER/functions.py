import time
import os


def caesarCipher(direction: str, textToCipher:str, shift: int):
    codedString = []

    if direction == "encode":
        for letter in textToCipher:
            letter = ord(letter)

            if letter < 97 or letter > 122:
                codedString.append(chr(letter))
            elif letter + shift > 122:
                letter = letter + shift - 26

                codedString.append(chr(letter))
            else:
                letter = letter + shift

                codedString.append(chr(letter))

    elif direction == "decode":
        for letter in textToCipher:
            letter = ord(letter)

            if letter < 97 or letter > 122:
                codedString.append(chr(letter))
            elif letter - shift < 97:
                letter = letter - shift + 26

                codedString.append(chr(letter))
            else:
                letter = letter - shift

                codedString.append(chr(letter))
    else:
        print("Invalid entry!")
        print("Try again.")
        time.sleep(5)
        os.system("clear")

        return False

    return ''.join(codedString)

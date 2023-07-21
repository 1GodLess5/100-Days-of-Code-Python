import functions

mainLoop = True

while mainLoop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input(f"Type the message you want to {direction}: ").lower().replace(" ", "")
    shift = int(input("Type the shift number: "))

    cipher = functions.caesarCipher(direction, text, shift)

    if cipher == False:
        continue
    else:
        print(f"Your {direction}d message is: {cipher}")
        goAgain = input("Do you want to continue? Type 'yes' or 'no': ").lower()

        if goAgain == "no":
            print("Thanks for using my CODER. <3")
            mainLoop = False

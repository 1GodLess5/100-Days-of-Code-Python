import random
import components

def cardsRender(cardToDraw: str):
    cardShape = components.cardShapes[random.randint(0, 7)]
    renderedCard = f''' ___\n|{cardToDraw}  |\n| {cardShape} |\n|__{cardToDraw}|'''

    return renderedCard


def gameStart():
    print(formattingConsole("BLUE"))
    print("Blackjack, by GodLess https://github.com/1GodLess5/100-Days-of-Code-Python/tree/master/day-11-CAPSTONE-PROJECT-BLACKJACK")
    print(components.logo)
    print(formattingConsole("END"))



    print(components.Color.BOLD + components.Color.RED)

    print('''
    RULES:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 to 10 are worth their face value.
      The dealer stops hitting at 17.

    COMMANDS TO CONTROL THE GAME:
      (H)it to take another card.
      (S)tand to stop taking cards.
      (D)ouble to increase your bet on your first play and must hit exactly one more time before standing.
      (F) to surrender, half of your bet will be returned.
      (E)ven money in case you have Blackjack and dealer's first card i Ace. You will be paid 1:1 instead of 1:2 in case of winning.
    ''')



def checkUsersAge():
    pass

def formattingConsole(format: str):
    listOfRequirements = format.split(", ")
    counter = 0
    finalString = ""

    for requirement in listOfRequirements:
        if counter > 0:
            finalString += " + "

        finalString += f"components.Color.{requirement}"

        counter += 1

    return eval(finalString)





















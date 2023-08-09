import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


biddersDictionary = {}
listOfBids = []
continueBiding = True
nameOfWinner = ""

while continueBiding:
    print(logo + "\n\n")
    print("Welcome to the secret auction program.")
    name = input("What is your name?:  ")
    bid = int(input("What's your bid?:    €"))
    biddersDictionary[name] = bid

    for key in biddersDictionary:
        listOfBids.append(biddersDictionary[key])
    listOfBids.sort()

    if bid == listOfBids[-1]:
        nameOfWinner = name

    moreBidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()

    if moreBidders == "no":
        continueBiding = False

    os.system("clear")


print(f"The winner of Secret Auctions is {nameOfWinner} with a bid of {biddersDictionary[nameOfWinner]}")

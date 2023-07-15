rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

class color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
    BLUE = '\033[94m'

def visualisation(choiceUser: int, choiceComputer: int):
    print("Your choice: ")
    if choiceUser == 0:
        print(rock)
    elif choiceUser == 1:
        print(paper)
    elif choiceUser == 2:
        print(scissors)
    else:
        print("You didn't input a valid number, no visualisation for you. :)")

    print("Computer's choice: ")
    if choiceComputer == 0:
        print(rock)
    elif choiceComputer == 1:
        print(paper)
    else:
        print(scissors)


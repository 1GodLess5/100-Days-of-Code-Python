import random
import rpsDesign

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print("Your choice:\n")
computerChoice = random.randint(0, 2)
rpsDesign.visualisation(userChoice, computerChoice)

if userChoice == computerChoice:
    print(f"{rpsDesign.color.BLUE} {rpsDesign.color.BOLD}IT'S A TIE.{rpsDesign.color.END}")
# user choose rock
elif userChoice == 0 and computerChoice == 1:
    print(f"{rpsDesign.color.RED} {rpsDesign.color.BOLD}YOU LOOSE!{rpsDesign.color.END}")
elif userChoice == 0 and computerChoice == 2:
    print(f"{rpsDesign.color.GREEN} {rpsDesign.color.BOLD}YOU WIN!{rpsDesign.color.END}")
# user choose paper
elif userChoice == 1 and computerChoice == 0:
    print(f"{rpsDesign.color.GREEN} {rpsDesign.color.BOLD}YOU WIN!{rpsDesign.color.END}")
elif userChoice == 1 and computerChoice == 2:
    print(f"{rpsDesign.color.RED} {rpsDesign.color.BOLD}YOU LOOSE!{rpsDesign.color.END}")
# user choose scissors
elif userChoice == 2 and computerChoice == 0:
    print(f"{rpsDesign.color.RED} {rpsDesign.color.BOLD}YOU LOOSE!{rpsDesign.color.END}")
elif userChoice == 2 and computerChoice == 1:
    print(f"{rpsDesign.color.GREEN} {rpsDesign.color.BOLD}YOU WIN!{rpsDesign.color.END}")
#invalid input
else:
    print(f"{rpsDesign.color.RED} {rpsDesign.color.BOLD}YOU DIDN'T ENTER A VALID CHOICE. :({rpsDesign.color.END}")

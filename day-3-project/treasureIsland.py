print('''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \\o\\_`"-._
             .'     / /                    \\ \\     '.
             |=====/o/======================\\o\\=====|
             |____/_/________..____..________\\_\\____|
             /   _/ \\_     <_o#\\__/#o_>     _/ \\_   \\
             \\________________\\####/________________/
              |===\\!/========================\\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \\========|o|===|
              |   | |         \\() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \\__     '-.\\uuu/.-'    __/ \\__ |
              |==== .'.'^'.'.====|
              |  _\\o/   __  {.' __  '.} _   _\\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

crossroad = input("You are at a crossroad. Where do you want to go? Type \"left\" or \"right\": ").lower()

if crossroad == "right":
    print("Game over! :(")
elif crossroad == "left":
    lake = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim "
        "across: ").lower()

    if lake == "swim":
        print("Game over! :(")
    elif lake == "wait":
        door = input("You arive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue."
                       " Which colour you choose? ").lower()

        if door != "yellow":
            print("Game over! :(")
        else:
            print("YOU HAVE FOUND THE TREASURE. GG <3")

    else:
        print("Not a valid choice. ._.")
else:
    print("Not a valid choice. ._.")





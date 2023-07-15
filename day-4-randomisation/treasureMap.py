row1 = ["_","️_","️_"]
row2 = ["_","_","️_"]
row3 = ["_️","_️","_️"]
treasureMap = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

positionX = int(input("Where do you want to put the treasure? X axis: ")) - 1
positionY = int(input("Where do you want to put the treasure? Y axis: ")) - 1
treasureMap[positionY][positionX] = "X"

print(f"{row1}\n{row2}\n{row3}")


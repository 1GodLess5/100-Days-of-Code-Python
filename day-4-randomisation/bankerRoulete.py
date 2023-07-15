import random

names = input("Give me everybody's names, separated by comma: ")
names = names.split(", ")

numberOfNames = len(names) -1
whoIsPaying = random.randint(0, numberOfNames)

print(f"{names[whoIsPaying]} is going to buy the meal today!")
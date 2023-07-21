import math


def areaCalculator(height: float, width: float, canCoverage: float):
    cansNeeded = math.ceil((height * width) / canCoverage)

    return cansNeeded

height = float(input("Enter wall height in meters: "))
width = float(input("Enter wall width in meters: "))
canCoverage = float(input("How many square meters can one can conver? "))

numberOfCans = areaCalculator(height, width, canCoverage)
print(f"You are going to need {numberOfCans} cans to cover the wall.")

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? "))
tipPercentage = int(input("What percentage tip would you like to give? Etc.10, 12, 15? "))
personsSplitting = int(input("How many people will split the bill? "))

totalBill = (bill / personsSplitting) * ((tipPercentage + 100) / 100)
print(f"Each person should pay: {round(totalBill, 2)}€")
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# average life 90 years
# 365 days, 52 weeks, 12 months
#You have 12410 days, 1768 weeks, and 408 months left.
age = int(age)

daysLeft = (90 * 365) - (age * 365)
weeksLeft = (90 * 52) - (age * 52)
monthsLeft = (90 * 12) - (age * 12)

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")




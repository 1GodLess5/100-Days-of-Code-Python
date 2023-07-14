# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator! ")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1.lower() + name2.lower()

counter = 0
counter += name.count("t")
counter += name.count("r")
counter += name.count("u")
counter += name.count("e")
trueCount = counter

counter = 0
counter += name.count("l")
counter += name.count("o")
counter += name.count("v")
counter += name.count("e")
loveCount = counter

score = int(str(trueCount) + str(loveCount))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


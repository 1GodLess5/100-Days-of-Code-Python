# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# This is how you work out whether if a particular year is a leap year.
#     on every year that is evenly divisible by 4
#     **except** every year that is evenly divisible by 100
#     **unless** the year is also evenly divisible by 400
# kazdy rok, ktery je delitelny 4
# pokud je delitelny 100 -> neni
# ale pokud je zaroven delitelny 400 -> je
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

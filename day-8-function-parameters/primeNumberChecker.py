def primeChecker(number: int):
    divisible = [2, 3, 4, 5, 6, 7, 8, 9]
    isPrime = True

    if number == 1:
        print(f"{number} is not a prime number.")
    else:
        for i in divisible:
            if number % i == 0 and number != i:
                isPrime = False
                print(f"{number} is not a prime number.")
                break

        if isPrime:
            print(f"{number} is a prime number.")


checkNumber = int(input("Check this number: "))
primeChecker(checkNumber)

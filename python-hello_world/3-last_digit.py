import random
number = random.randint(-10000, 10000)
lastDigitOf = abs(number) % 10
if lastDigitOf > 5:
    print("Last digit of", number, "is", lastDigitOf, "and is greater than 5")
elif lastDigitOf == 0:
    print("Last digit of", number, "is", lastDigitOf, "and is 0")
elif (lastDigitOf < 6) & (lastDigitOf != 0):
    print("Last digit of", number, "is", lastDigitOf, "and is less than 6 and not 0")
    
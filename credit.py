import math
from cs50 import get_int

def main():
    digitCount = 0
    digit1 = 0
    digit2 = 0
    oddSum = 0
    evenSum = 0
    validator = 0
    firstTwo = 0

    card = get_int("Number: ")

    while card > 0:
        digit2 = digit1
        digit1 = card % 10

        if digitCount % 2 == 0:
            evenSum += digit1
        else:
            multi = 2 * digit1
            oddSum += (multi // 10) + (multi % 10)
        card //= 10
        digitCount += 1

    validator = (evenSum + oddSum) % 10 == 0
    firstTwo = (digit1 * 10) + digit2


    if digit1 == 4 and digitCount > 12 and digitCount < 17:
        print("VISA")
    elif firstTwo > 50 and firstTwo < 56 and digitCount == 16:
        print("MASTERCARD")
    elif (firstTwo == 34 or firstTwo == 37) and digitCount == 15:
        print("AMEX")
    else:
        print("INVALID")

if __name__ == "__main__":
    main()
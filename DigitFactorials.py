import math

def CompareDigitsToFactorial(number):
    Digits = [int(i) for i in str(number)]
    DigitFactorialSum = 0
    for i in Digits:
        DigitFactorialSum += math.factorial(i)
    if number == DigitFactorialSum:
        return True
    return False

SumOfTrues = 0
for i in range(10,1000000):
    if CompareDigitsToFactorial(i):
        print(i)
        SumOfTrues += i
print('The Sum of these numers is', SumOfTrues)

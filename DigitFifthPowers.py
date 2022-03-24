def CompareDigitsToPower(number,power):
    Digits = [int(i) for i in str(number)]
    DigitPowerSum = 0
    for i in Digits:
        DigitPowerSum += i**power
    if number == DigitPowerSum:
        return True
    return False

SumOfTrues = 0
for i in range(10,1000000):
    if CompareDigitsToPower(i,5):
        print(i)
        SumOfTrues += i
print('The Sum of these numers is', SumOfTrues)

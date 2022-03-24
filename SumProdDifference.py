import math

def DigitList(n):
    return [int(i) for i in str(n)]

Number = 198
NumberAsList = DigitList(Number)
print(math.prod(NumberAsList) - sum(NumberAsList))

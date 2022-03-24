def Division(dividend,divisor):
    Fraction = [[],['N']]
    DividendsList = []
    if dividend < divisor:
        dividend *= 10
    while dividend != 0 and dividend not in DividendsList:
        DividendsList.append(dividend)
        if dividend < divisor//10:
            Fraction[0] += [0]
        while dividend < divisor:
            dividend *= 10
        Fraction[0].append(dividend//divisor)
        dividend = dividend - (dividend//divisor)*divisor
        if dividend in DividendsList:
            Fraction[1][0] = 'R'

    if Fraction[1] == ['R']:
        Fraction[0].pop(-1)

    return Fraction

MaxLength = 0
WhichDividend = 2

for i in range(2,1001):
    Decimal = Division(1,i)
    if (Decimal[1] == ['R']) and (len(Decimal[0]) > MaxLength):
        WhichDividend = i
        MaxLength = len(Decimal[0])
        print(WhichDividend,Decimal[0], 'has length', MaxLength)
print(WhichDividend,'has length',MaxLength)

nfac = gamma(100)

def decomp(integer1):
    Digits = []
    while integer1 > 0:
        Digits.append(integer1%10)
        integer1 = integer1//10
    Digits.reverse()
    return Digits

print sum(decomp(nfac))
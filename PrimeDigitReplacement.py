from itertools import combinations

def IsPrime(num):
    if num == 1:
        return False
    for i in range(2,int(num**(1/2))+1):
        if num%i == 0:
            return False
    return True

def ReplaceDigits(number,indices):
    NumberList = []
    PrimeReplacementList = []
    for i in range(len(str(number))):
        NumberList.append(str(number)[i])
    for digit in range(0,10):
        for i in indices:
            NumberList[i] = str(digit)
        if len(str(int(''.join(NumberList))))==len(str(number)) and IsPrime(int(''.join(NumberList))):
            PrimeReplacementList.append(int(''.join(NumberList)))
    return(PrimeReplacementList)

for number in range(10,1000000):
    if IsPrime(number):
        for howmany in range(1,len(str(number))+1):
            for slots in combinations(range(len(str(number))),howmany):
                PrimeReplacements = ReplaceDigits(number,slots)
                if number in PrimeReplacements and len(PrimeReplacements) >= 8:
                    print(number,slots,PrimeReplacements,'has length',len(PrimeReplacements))

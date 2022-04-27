import math

def IsPrime(num):
    if num == 1:
        return False
    for i in range(2,int(num**(1/2))+1):
        if num%i == 0:
            return False
    return True

def RightTruncatablePrime(prime):
    for i in range(len(str(prime))):
        if IsPrime(prime//(10**i)) == False:
            return False
    return True

def LeftTruncatablePrime(prime):
    for i in range(len(str(prime)),0,-1):
        if IsPrime(prime%(10**i)) == False:
            return False
    return True

DoubleTruncatablePrimes = []
i = 10
while len(DoubleTruncatablePrimes) < 11:
    if IsPrime(i):
        if RightTruncatablePrime(i) and LeftTruncatablePrime(i):
            DoubleTruncatablePrimes.append(i)
    i += 1

print('There are',len(DoubleTruncatablePrimes),'truncatable primes.  They are',DoubleTruncatablePrimes,'Their sum is',sum(DoubleTruncatablePrimes))

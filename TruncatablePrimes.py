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
for i in range(10,1000000):
    if IsPrime(i):
        if RightTruncatablePrime(i) and LeftTruncatablePrime(i):
            DoubleTruncatablePrimes.append(i)

print('There are',len(DoubleTruncatablePrimes),'truncatable primes.  They are',DoubleTruncatablePrimes,'Their sum is',sum(DoubleTruncatablePrimes))

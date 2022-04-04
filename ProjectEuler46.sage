def IsGoldbach(Number1):
    P = Primes()
    if Number1%2 == 0:
        return True
    if Number1 in P:
        return True
    limit = int(sqrt(Number1))+1
    Squares = [s^2 for s in xrange(1,limit)]
    index = 0
    while P[index] < Number1:
        for s in Squares:
            if P[index] + 2*s == Number1:
                return True
        index = index + 1
    return False

i = 4
Odd = 2*i+1
while IsGoldbach(Odd) == True:
    # print Odd
    i = i+1
    Odd = 2*i+1

print 'The first time the conjecture is false is', Odd

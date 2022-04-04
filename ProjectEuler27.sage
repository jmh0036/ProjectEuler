var('a,b')

f(a,b,x) = x^2 + a*x + b

P = Primes()

MaxA = 0
MaxB = 0
MaxLen = 0
for a in xrange(-999,999,2):
    for b in prime_range(2,1000):
        print f(a,b,x)
        PrimesInImage = []
        n = 0
        while f(a,b,x=n) in P:
            PrimesInImage.append(f(a,b,x=n))
            n = n+1
        if len(PrimesInImage) > MaxLen:
            MaxLen = len(PrimesInImage)
            MaxA = a
            MaxB = b

print MaxA*MaxB, f(a=MaxA,b=MaxB,x=x), MaxLen

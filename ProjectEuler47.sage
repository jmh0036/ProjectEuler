P = Primes()

MaxLength = 0
MaxA = 0
MaxB = 0
Image = 0
for a in xrange(-1000,1001):
    for b in xrange(-999,1001,2):
        f(x) = x^2+a*x+b
        print f
        n = 0
        PrimesInImage = []
        while Image in P:
            Image = f(n)
            PrimesInImage.append(Image)
            n = n+1
        if len(PrimesInImage) > MaxLength:
            MaxLength = len(PrimesInImage)
            MaxA = a
            MaxB = b

print MaxLength, MaxA, MaxB, MaxA*MaxB
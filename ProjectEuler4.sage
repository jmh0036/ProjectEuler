def Reverse(Number):
    Reverse = 0
    while(Number > 0):
        Remainder = Number %10
        Reverse = (Reverse *10) + Remainder
        Number = Number //10
    return Reverse

def CheckPalindrome(CheckNum):
    if CheckNum == Reverse(CheckNum):
        return True
    return False

Product = 0
MaxPalindrome = 0
for int1 in xrange(100,1000):
    for int2 in xrange(int1,1000):
        Product = 0
        Product = int1*int2
        if CheckPalindrome(Product) == True and Product > MaxPalindrome:
            print 'Current Max is', Product, 'product:', int1, '*',int2
            MaxPalindrome = Product

print '----- The Absolute Max -----'

print 'The absolute Max is', MaxPalindrome
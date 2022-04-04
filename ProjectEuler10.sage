PrimeNumbers = Primes()
GreatestNumber = 2000000
# GreatestNumber = 10

CurrentPrime = 0
Summation = 0
while PrimeNumbers[CurrentPrime] < GreatestNumber:
    Summation += PrimeNumbers[CurrentPrime]
    print 'After adding', PrimeNumbers[CurrentPrime], 'our sum is', Summation
    CurrentPrime += 1

print Summation
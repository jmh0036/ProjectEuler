from sympy.ntheory import factorint

def phiFunction(x):
    dictionary = factorint(x)
    Primes = list(dictionary.keys())
    product = 1
    for prime in Primes:
        product *= (1-(1/prime))
    return int(x*product)

MaxValue = 2
where = 2
for i in range(2,1000001):
    PhiValue = i/phiFunction(i)
    if i % 1000 == 0:
        print(i,phiFunction(i),PhiValue)
    if PhiValue > MaxValue:
        where = i
        MaxValue = PhiValue
print(where,MaxValue)

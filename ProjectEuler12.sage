TriangularNumber = lambda i : i*(i+1)/2

#### Begin Way 1 ####

# i = 1
# while len(divisors(TriangularNumber(i))) <= 500:
#     print TriangularNumber(i), 'has', len(divisors(TriangularNumber(i))), 'divisors'
#     i = i + 1

# print TriangularNumber(i), 'has', len(divisors(TriangularNumber(i))), 'divisors'

#### End of Way 1 ####


#### Begin Way 2 ####

FactorDict = { }

i = 1
while len(divisors(TriangularNumber(i))) <= 500:
    FactorDict[TriangularNumber(i)] = len(divisors(TriangularNumber(i)))
    i = i + 1

FactorDict[TriangularNumber(i)] = len(divisors(TriangularNumber(i)))

print max(FactorDict)

#### End Way 2 ###
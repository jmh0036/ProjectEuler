AbundantNumbers = []

for n in xrange(1,28123):
    Divs = divisors(n)
    Divs.remove(n)
    if sum(Divs) > n:
        AbundantNumbers.append(n)

UnRepresentable = range(0,28123)
for i in xrange(0,len(AbundantNumbers)):
    j = i
    while AbundantNumbers[i]+AbundantNumbers[j] < 28124:
        a1 = AbundantNumbers[i]
        a2 = AbundantNumbers[j]
        print a1,a2,a1+a2
        if a1+a2 in UnRepresentable:
            UnRepresentable.remove(a1+a2)
        j = j+1

print UnRepresentable
print sum(UnRepresentable)

Sum = 0
for i in xrange(1,1000):
    Sum += i^i

print Sum
print mod(Sum,10^10)
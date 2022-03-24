import math

Sum = 0

for i in xrange(0,1000):
    if i%3 == 0 or i%5 == 0:
        Sum = Sum + i
        print i, Sum

print Sum
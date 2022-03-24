import math
import sys

# ********* BEGIN THINGS TO ENTER ********* 
#prime to mod out by
# p = 7
# Starting Values
P0 = 1
P1 = 1
# Weights a*P_{n-1} + b*P_{n-2}
a = 1
b = 1
# ********* END THINGS TO ENTER ********* 



#initialize list
Recursion = []
Recursion.append(P0)
Recursion.append(P1)

# Compute long list
i = 2
Stop = 0
while Stop < 4000000:
	Recursion.append(((a*Recursion[i-1])+(b*Recursion[i-2])))
	Stop = Recursion[i]
	i = i + 1

# print Recursion

EvenSum = 0
for i in xrange(0,len(Recursion)):
	if Recursion[i]%2 == 0:
		EvenSum = EvenSum + Recursion[i]

print EvenSum
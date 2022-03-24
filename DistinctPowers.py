LowerLimit = 2
UpperLimit = 100

IntegerList = []
for a in range(LowerLimit,UpperLimit+1):
    for b in range(LowerLimit,UpperLimit+1):
        if a**b not in IntegerList:
            IntegerList.append(a**b)
print(sorted(IntegerList), 'has length', len(IntegerList))

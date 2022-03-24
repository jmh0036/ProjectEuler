from itertools import permutations
from sympy.ntheory import factorint

def IsCubic(number):
    FactorDic = factorint(number)
    for p in FactorDic.keys():
        if FactorDic[p]%3 != 0:
            return False
    return True

def PermuteNumber(number):
    for i in {"".join(p) for p in permutations(str(number))}:
        yield i

DesiredLength = 3

i = 1
PermCubes = [i]
while len(PermCubes) < 5:
    PermCubes = []
    if IsCubic(i):
        for NewNumber in PermuteNumber(i):
            NewNumberInt = int(NewNumber)
            if ( len(str(NewNumberInt)) == len(str(i)) ) and IsCubic(NewNumberInt):
                PermCubes.append(NewNumberInt)
        # print(i,PermCubes,len(PermCubes))
    if len(PermCubes) >= DesiredLength:
        print(i,PermCubes,len(PermCubes))
    i += 1

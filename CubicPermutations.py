from itertools import permutations

def IsCubic(number):
    return int(round(number ** (1. / 3))) ** 3 == number

def PermuteNumber(number,permutation):
    NumberList = [i for i in str(number)]
    PermutedList = [NumberList[i] for i in permutation]
    return int(''.join(PermutedList))

DesiredLength = 5

PermCubics = []
i = 1
while len(PermCubics) != DesiredLength:
    # if i % 100000 == 0:
    #     print(i)
    Cube = i**3
    PermCubics = []
    for perm in permutations(range(len(str(Cube)))):
        NewNumber = PermuteNumber(Cube,perm)
        if (NewNumber not in PermCubics) and (len(str(NewNumber))==len(str(Cube))) and IsCubic(NewNumber):
            PermCubics.append(NewNumber)
    print(Cube,PermCubics,len(PermCubics))
    if len(PermCubics) != DesiredLength:
        i = i+1

print(i**3,PermCubics)

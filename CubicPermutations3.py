from itertools import permutations
import math

def IsPrime(num):
    if num <= 1:
        return False
    for i in range(2,int(num**(1/2))+1):
        if num%i == 0:
            return False
    return True

# print(7 in ((filter(IsPrime, range(1,20)))))

def IsCubic(number):
    if IsPrime(number):
        return False
    for p in filter(IsPrime,range(2,number)):
        exponent = 3
        while p**exponent < number:
            exponent += 3
        # print(exponent)
        if (number%p == 0) and (number%(p**exponent) != 0):
            print(number,'is divisible by',p,'but not by',p,'raised to the',exponent)
            return False
    return True

# for i in range(2,1002):
#     if IsCubic(i):
#         print(i)

print(IsCubic(1000))

# def PermuteNumber(number):
#     for i in {"".join(p) for p in permutations(str(number))}:
#         yield i

# DesiredLength = 3

# for i in range(2,10000):
#     if IsCubic(i):
#         print(i,factorint(i))

# i = 41063625
# PermCubes = [i]
# while len(PermCubes) < 5:
#     PermCubes = []
#     if IsCubic(i):
#         for NewNumber in PermuteNumber(i):
#             NewNumberInt = int(NewNumber)
#             if ( len(str(NewNumberInt)) == len(str(i)) ) and IsCubic(NewNumberInt):
#                 PermCubes.append(NewNumberInt)
#         print(i,PermCubes,len(PermCubes))
#     if len(PermCubes) >= DesiredLength:
#         print(i,PermCubes,len(PermCubes))
#     i += 1

SumsOfMult = 0

for i in range(0,1000):
    if mod(i,3)==0 or mod(i,5)==0:
        SumsOfMult = SumsOfMult+i

print SumsOfMult
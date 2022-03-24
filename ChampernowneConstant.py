ChampernowneConstant = 0
EndValue = 1000000

ChampernowneConstant = ''
for i in range(1,EndValue):
    ChampernowneConstant += str(i)

product = int(ChampernowneConstant[1000000-1])*int(ChampernowneConstant[100000-1])*int(ChampernowneConstant[10000-1])*int(ChampernowneConstant[1000-1])*int(ChampernowneConstant[100-1])*int(ChampernowneConstant[10-1])*int(ChampernowneConstant[1-1])

print('The terms of interest are', ChampernowneConstant[1000000-1],ChampernowneConstant[100000-1],ChampernowneConstant[10000-1],ChampernowneConstant[1000-1],ChampernowneConstant[100-1],ChampernowneConstant[10-1],ChampernowneConstant[1-1],'and their product is',product)

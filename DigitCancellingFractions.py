import math
import numpy as np

ValidDumbReductions = []

for numerator in range(10,99):
    for denominator in range(numerator+1,100):
        NumList = [i for i in str(numerator)]
        DenList = [i for i in str(denominator)]
        NumsInCommon = []
        for i in NumList:
            if i in DenList:
                NumsInCommon.append(i)
        if NumsInCommon != []:
            for i in NumsInCommon:
                DumbNumerator = [i for i in NumList]
                DumbDenominator = [i for i in DenList]
                DumbNumerator.remove(i)
                DumbDenominator.remove(i)
                DumbFraction = DumbNumerator[0] + '/' + DumbDenominator[0]
                if (numerator%10 != 0 and denominator%10 != 0) and (int(DumbDenominator[0]) != 0) and numerator/denominator == int(DumbNumerator[0])/int(DumbDenominator[0]):
                    print(str(numerator)+'/'+str(denominator),'=',DumbFraction)
                    ValidDumbReductions.append([int(DumbNumerator[0]),int(DumbDenominator[0])])

print('Reduced Valid Dumb Reductions:',ValidDumbReductions)

ValidDumbNumerator = [i[0] for i in ValidDumbReductions]
ValidDumbDenominator = [i[1] for i in ValidDumbReductions]
for i in range(len(ValidDumbNumerator)):
    for j in range(len(ValidDumbDenominator)):
        gcd = math.gcd(ValidDumbNumerator[i],ValidDumbDenominator[j])
        if gcd > 1:
            ValidDumbNumerator[i] = int(ValidDumbNumerator[i]/gcd)
            ValidDumbDenominator[j] = int(ValidDumbDenominator[j]/gcd)

print(ValidDumbNumerator)
print(ValidDumbDenominator)

print('The Denominator of the Reduced fraction will be', np.prod(ValidDumbDenominator))

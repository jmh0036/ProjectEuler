def SumOfSquares(maxValue):
    SumOfSquares = 0
    for i in xrange(0,maxValue+1):
        SumOfSquares += i^2
    return SumOfSquares

def SquareOfSum(maxValue):
    RunningSum = 0
    for i in xrange(0,maxValue+1):
        RunningSum += i
    return (RunningSum)^2

# EndValue = 100
for EndValue in xrange(10,100):
    for Modulo in xrange(2,20,2):
        print EndValue, 'mod', Modulo, 'The difference of', SquareOfSum(EndValue)%Modulo, 'and', SumOfSquares(EndValue)%Modulo, 'is', (SquareOfSum(EndValue)-SumOfSquares(EndValue))%Modulo

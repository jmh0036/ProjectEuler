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

EndValue = 100

print 'The difference of', SquareOfSum(EndValue), 'and', SumOfSquares(EndValue), 'is', SquareOfSum(EndValue)-SumOfSquares(EndValue)
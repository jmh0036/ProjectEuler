SumOfEvenFib = 0

index = 0

while fibonacci(index)<4000000:
    if mod(fibonacci(index),2)==0:
        SumOfEvenFib = SumOfEvenFib+fibonacci(index)
    index = index + 1

print SumOfEvenFib
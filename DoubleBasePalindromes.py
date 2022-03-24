def IsPalindrome(number):
    Original = [int(i) for i in str(number)]
    Reverse = Original[::-1]
    if Original == Reverse:
        return True
    return False

def ToBinary(number):
    BinaryRepList = []
    while number > 0:
        BinaryRepList += [number % 2]
        number = number // 2
    BinaryRep = ''
    for i in BinaryRepList:
        BinaryRep += str(i)
    return BinaryRep

SumOfDoublePalindromes = 0
for i in range(1,1000001):
    if IsPalindrome(i) and IsPalindrome(ToBinary(i)):
        SumOfDoublePalindromes += i
        print('Base Ten:',i,'Binary:',ToBinary(i))
print('The Sum of these Palindromes is', SumOfDoublePalindromes)

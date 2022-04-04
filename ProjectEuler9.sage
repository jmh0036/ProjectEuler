SumOfTriples = 1000

ListOfPartitions = Partitions(SumOfTriples,length=3).list()

for i in ListOfPartitions:
    if (i[0]^2+i[1]^2 == i[2]^2) or (i[0]^2+i[2]^2 == i[1]^2) or (i[1]^2+i[2]^2 == i[0]^2):
        print i, 'is a pythagorean triple with a product of', prod(i)
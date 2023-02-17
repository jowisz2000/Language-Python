import random
import math

firstList = [random.randrange(20) for i in range(100)]
secondList = [random.randrange(20) for j in range(100)]
list(filter(lambda z: 3 < z[0]+z[1] < 15, zip(firstList, secondList)))

x = [i for i in range(10)]
y = [2*i + random.randrange(3) for i in x]

avgX = sum(x)/len(x)
D = sum(map(lambda i: (i-avgX)**2, x))
a = sum(map(lambda i: i[1]*(i[0]-avgX), zip(x, y)))/D
b = sum(y)/len(y) - a*avgX
deltaY = math.sqrt(sum(map(lambda i: (i[1] - a*i[0]-b)**2/(len(x)-2), zip(x, y))))
deltaA = deltaY / math.sqrt(D)
deltaB = deltaY * math.sqrt(1/len(x) + avgX**2/D)
#print(deltaB, deltaA, deltaY)

def myreduce(fun, seq):
    result = seq[0]
    for i in range(1, len(seq)):
        result = fun(result, seq[i])
    return result


print(myreduce(lambda c, d: c-d, [19, 190, -171]))

thirdList = [[1,2], [3,4], [5,6]]

endList = [list(map(lambda x: x[0], thirdList)), list(map(lambda x: x[1], thirdList))]
print(list(endList))

import random

firstList = [i for i in range(10)]
n = 2
# delete element from list
firstList[:] = [i for i in firstList if i != n]
print(firstList)

# delete element with odd indexes
firstList = [i for i in range(10)]
for i in range(1, len(firstList), 2):
    print(firstList[i])

secondList = [(random.randrange(10), firstList[i]) for i in range(10)]
secondList.sort(key=lambda x: x[1])
print(secondList)

thirdList = [i for i in secondList if i[0] % 2 == 0]
print(thirdList)

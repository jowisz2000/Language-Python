import random
import string

k = 10
firstList = [random.randrange(5*k) for i in range(k)]
secondList = firstList.copy()
dictionary = {}
for j in range(30):
    count = 0
    random.shuffle(firstList)
    for i in range(k):
        if firstList[i] == secondList[i]:
            count += 1
    dictionary[count] = dictionary.get(count, 0) + 1

'''print(firstList)
print(secondList)
print(dictionary)'''

a = '.'.join([random.choice(string.ascii_lowercase) for i in range(k)])
# print(a)

thirdList = [random.randrange(10) for i in range(100)]
summary = {}

for count, value in enumerate(thirdList):
    summary.setdefault(value, []).append(count)

palindromeSummary = {}

for i in range(50):
    n = random.randint(2, 4)
    number = str(random.randint(10**(n-1), 10**n-1))
    isPalindrome = True
    #print(number, len(number))
    for j in range(1, len(number)//2 + 1):
        if number[j-1] != number[-j]:
            isPalindrome = False
    if isPalindrome:
        #print(number)
        palindromeSummary[len(number)] = palindromeSummary.get(len(number), 0) + 1

#print(palindromeSummary)

firstDict, secondDict = {}, {}
for i in range(20):
    firstDict[i] = random.randrange(100)
    secondDict[i] = random.randrange(100)

firstDict = {value: key for key, value in firstDict.items()}
secondDict = {value: key for key, value in secondDict.items()}
repeatedDict = {i: (firstDict[i], secondDict[i]) for i in firstDict if i in secondDict}
print(repeatedDict)



import string

myString = "1q3awergpn30w4ohanra0focq483-Pnfbc2kBIDUCVQODBowiukw-sgvzi ekwd/"
smallLetters = [i for i in myString if i in string.ascii_lowercase]
# print(smallLetters)
smallSingleLetters = ""
for i in smallLetters:
    if i not in smallSingleLetters:
        smallSingleLetters += i
# print(smallSingleLetters)

numbers = [i for i in myString if i in string.digits]
# print(numbers)

a, b = 0, 0
for i in smallSingleLetters:
    if i in "eouia":
        a += 1
    else:
        b += 1

tuples = [(int(i), a*int(i)+b) for i in numbers]
# print(a, b)
# print(tuples)


x = [i for i in range(6)]
y = [0, 1.5, 3, 4.7, 6.1, 7.1]
coordinates = [[x[i], y[i]] for i in range(len(x))]

avgX = sum(x)/len(x)
avgY = sum(y)/len(y)
# print(avgX)
D = sum([(i-avgX)**2 for i in x])
# print(D)
a = sum([i[1]*(i[0]-avgX) for i in coordinates])/D
# print(a)
b = avgY - a * avgX
# print(b)
import math
import random


def logarithm(): 
    a, u, x, i = 0.05, 0, 1, 0
    while x < 1.5:
        u += a/x
        i += 1
        x += a
        yield x, u, math.log(x)


'''for _ in logarithm():
    print(_, end='\n')'''


N = 100
randomList = [random.randrange(2) for i in range(N)]


def lenOfZeros(lst):
    length = 0
    for i in lst:
        if i == 1:
            yield length
            length = 0
        else:
            length += 1


# print(sum(lenOfZeros(randomList))/N)

def fibo():
    a, b = 0, 1
    while True:
        yield b
        c = a+b
        a = b
        b = c


def odd(seq):
    for i in seq:
        if i % 2:
            yield i


def even(seq):
    for i in seq:
        if i % 2 == 0:
            yield i


def filterValues(seq, value):
    for i in seq:
        if i < value:
            print(i, end=' ')
            yield i
        else:
            print('\n')
            return 0


print(sum(filterValues(even(fibo()), 100)))

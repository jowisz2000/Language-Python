

class Random:

    def __init__(self, m, a, x0, c):
        self.m, self.a, self.x, self.c = m, a, x0, c

    def __iter__(self):
        return self

    def __next__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x


def calka(begin, end, high, low, fun, n=1000):

    if begin > end or low > high:
        raise ValueError

    t = 0
    iterator = Random(2 ** 48, 44485709377909, 0, 1)
    for i in range(n):
        x = next(iterator)/2**48 * (end-begin)
        y = next(iterator)/2**48 * (high-low)
        if 0 < y <= fun(x):
            t += 1
        if 0 > y >= fun(x):
            t -= 1
    return (end-begin)*(high-low)*t/n
    # return t





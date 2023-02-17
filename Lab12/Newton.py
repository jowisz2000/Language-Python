import math

import scipy


class NewtonRaphson:

    def __init__(self, fun, x, eps):
        self.fun, self.x, self.eps = fun, x, eps

    def __iter__(self):
        return self

    def __next__(self):
        self.x -= self.fun(self.x)/scipy.misc.derivative(self.fun, self.x)

        if math.fabs(self.fun(self.x)) < 10**(-5):
            raise StopIteration

        return self.x

import abc


class Calka(abc.ABC):

    def __init__(self, begin, end, steps, fun):
        self.begin, self.end, self.steps, self.fun = begin, end, steps, fun

    @abc.abstractmethod
    def calculate(self):
        '''
        calculates integral of function in given range
        :return: value of integral
        '''
        pass


class Trapez(Calka):

    def calculate(self):
        h, s, x = (self.end-self.begin)/self.steps, 0, self.begin
        for i in range(self.steps):
            s += self.fun(x) + self.fun(x+h)
            x += h
        return s*h/2


class Simpson(Calka):

    def calculate(self):
        h, s, x = (self.end-self.begin)/self.steps/2, 0, self.begin
        for i in range(2 * self.steps + 1):
            if i == 0 or i == 2 * self.steps:
                s += self.fun(x)
            elif i % 2 == 0:
                s += 2 * self.fun(x)
            else:
                s += 4 * self.fun(x)
            x += h
        return s*h/3


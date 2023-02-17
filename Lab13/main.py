import Calka, Stack, random

# zadanie 1.

tmp1 = Calka.Trapez(0, 2, 3000, lambda x: 4*x**3)
# print(tmp1.calculate())

tmp2 = Calka.Simpson(0, 2, 3000, lambda x: 4*x**3)
# print(tmp2.calculate())


# zadanie 2.

length = 0
for i in range(100):
    tmp3 = Stack.SortedStack()
    for j in range(100):
        rng = random.randrange(100)
        tmp3.push_single(rng)
    length += tmp3.size()

# print(length/100)

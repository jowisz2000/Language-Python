import arithmetic
import integral
import math
import Newton


# tmp1 = arithmetic.iterator1(1, 1, 10)
# for i in tmp1:
#     for j in tmp1:
#         print(i, j)

# tmp2 = arithmetic.iterator2(1, 3, 10)
# for i in tmp2:
#     for j in tmp2:
#         print(i, j)

# print(integral.calka(0, 3.14, 3, -3, lambda x: 4*x**3 - 2, 100000))

dx = Newton.NewtonRaphson(lambda x: math.sin(x)+x**2/10, 1.5, 10**-7)

for i in dx:
    print(i)

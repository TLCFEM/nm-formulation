# for the given function 1.15x^2+y^2+3.67x^2y^2=1.15
# find pairs of (x,y) that satisfy the equation
# and plot them

from sympy import Symbol
import numpy as np
import matplotlib.pyplot as plt


def f(r: float, t: float):
    x = r * np.cos(t)
    y = r * np.sin(t)
    return 1.15 * x ** 2 + y ** 2 + 3.67 * x ** 2 * y ** 2 - 1.15


def dfdr(r: float, t: float):
    x = r * np.cos(t)
    y = r * np.sin(t)
    return (2.3 * x + 7.34 * x * y ** 2) * np.cos(t) + (2 * y + 7.34 * x ** 2 * y) * np.sin(t)


def newton(r0, t):
    r = r0
    residual = f(r, t)
    while abs(residual) > 0.000001:
        jacobian = dfdr(r, t)
        r = r - residual / jacobian
        residual = f(r, t)
    return r

array = []

for t in np.arange(0, np.pi / 2, 0.01):
    r0 = 1
    r = newton(r0, t)
    x = r * np.cos(t)
    y = r * np.sin(t)
    array.append((x, y))
    plt.plot(y, x, 'r.')

plt.show()


# save to file
with open('../EQ16.txt', 'w') as f:
    for item in array:
        f.write(f'{item[1]:.3f}\t{item[0]:.3f}\n')

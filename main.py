import math
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()


def func(x):
    return 0.3 * math.exp(-0.7 * math.sqrt(x)) - 2 * (x ** 2) + 4


def fprime(x):
    return (-21 / (200 * math.exp((7.0 / 10.0) * math.sqrt(x)) * math.sqrt(x))) - 4 * x


def fprime2(x):
    return ((147 * math.exp((7.0 / 10.0) * math.sqrt(x)) * math.sqrt(x) + 210 * math.exp((7.0 / 10.0) * math.sqrt(x)))/ 4000 * math.sqrt((7.0 / 5.0) * math.sqrt(x)) * x * math.sqrt(x)) - 4


def phi(x):
    return math.sqrt((0.3 * math.exp(-0.7 * math.sqrt(x)) + 4) / 2)


# Деление попалам
def bisections(func, bounds, e=0.01):
    a, b = bounds
    if func(a) * func(b) > 0:
        print("На заданном интервале нет корней!")
        return

    x0 = (a + b) / 2
    count = 0
    total = [x0]

    while abs(a - b) >= e:
        count += 1
        print(f'{count} итерация, {x0}')
        if func(a) * func(x0) > 0:
            a = x0
        else:
            b = x0
        x0 = (a + b) / 2
        total.append(x0)
    return total


# Ньютон
def newton(func, fprime, fprime2, bounds, eps=0.001):
    a, b = bounds
    count = 0
    total = []
    if func(a) * fprime2(a) > 0:
        x0 = a
    elif func(b) * fprime2(b) > 0:
        x0 = b
    else:
        print("Неверно выбран начальный интервал")
        return
    x = x0 - func(x0) / fprime(x0)
    total.append(x)
    while abs(x - x0) >= eps:
        count += 1
        print(f'{count} итерация, {x}')
        x0 = x - func(x) / fprime(x)
        x = x0 - func(x0) / fprime(x0)
        total.append(x)
    return total


# Секущих
def secant(func, x0, x1, eps=0.01):
    total = []
    count = 0
    x_prev, x = x0, x1
    total.append(x)
    while abs(x - x_prev) >= eps:
        count += 1
        print(f'{count} итерация, {x}')
        x, x_prev = (x - func(x) * (x - x_prev) / (func(x) - func(x_prev)), x)
        total.append(x)
    return total


# Простых итераций
def iterations(phi, a, eps=0.01):
    i = 1
    x = phi(a)
    x0 = phi(x)
    total = [x0]
    while abs(x - x0) >= eps:
        print(f'{i} итерация, {x0}')
        x = phi(x0)
        x0 = phi(x)
        i += 1
        total.append(x0)
        if i == 10000:
            print("Выполнено 1000 итераций, решение не найдено")
            return
    return total


# x = bisections(func, (1, 2))
# x = newton(func, fprime, fprime2, (1, 2))
# x = secant(func, 1, 2)
# x = iterations(phi, 1)
# print(f'Конечный результат: {x[-1]}')


plt.grid()
x_s = np.linspace(0, 6, 20)
y_s = [func(x) for x in x_s]
plt.ylim((-5, 6))
plt.xlim((0, 4))
plt.plot(x_s, y_s,)
plt.scatter(1, 0, label=f'Точка a')
plt.scatter(2, 0, label=f'Точка b')


for i in range(len(x)):
    plt.scatter(x[i], 0, label=f'{i + 1} итерация')
plt.legend()
plt.show()











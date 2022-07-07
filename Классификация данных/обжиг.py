import random
import math


def getQ(i):
    return 1/i


def getRandomPoint(x, d):
    return [
        x[i] + random.random()*d - d/2
        for i in range(len(x))
    ]


def solve(func, x, d, qMin):
    k = 1
    q = getQ(k)
    while q > qMin:
        newX = getRandomPoint(x, d)
        p = None
        df = func(newX) - func(x)
        if df < 0:
            p = 1
        else:
            p = math.exp(-df/q)


        if random.random() <= p:
            print('Итерация', k)
            print('Текущая точка:', x)
            print('Значение функции в этой точке:', func(x))
            print('Новая точка:', newX)
            print('Значение функции в этой точке:', func(newX))
            x = newX

        k += 1
        q = getQ(k)
    print('\nОптимальная точка:', x)
    print('Значение функции в этой точке:', func(x))


def f(x):
    x1 = x[0]
    x2 = x[1]
    return 3*x1*x1 + x1*x2 + 3*x2*x2 - 8*x1

solve(f, [0,0], 2, 0.01)


import random
import numpy as np


def getP(func, particles, pOld=None):
    if pOld is None:
        return particles
    res = []
    for i in range(len(particles)):
        if func(particles[i]) < func(pOld[i]):
            res.append(np.copy(particles[i]))
        else:
            res.append(np.copy(pOld[i]))
    return res


def getG(func, particles, gOld=None):
    if gOld is None:
        return np.copy(min(particles, key=func))
    else:
        mp = min(particles, key=func)
        if func(mp) < func(gOld):
            return np.copy(mp)
        return np.copy(gOld)


def solve(func, m, startLimits, vMax, iters):
    t = 1
    particles = []
    for _ in range(m):
        p = []
        for lim in startLimits:
            p.append(lim[0] + (lim[1] - lim[0]) * random.random())
        particles.append(np.array(p))
    v = []
    for _ in range(m):
        vi = []
        for _ in range(len(startLimits)):
            vi.append(random.random() * vMax)
        v.append(np.array(vi))

    p = getP(func, particles)
    g = getG(func, particles)
    for it in range(iters):
        print('Итерация', it)
        for i in range(len(particles)):
            a = random.random()
            b = random.random()
            v[i] += a * (p[i] - particles[i]) + b * (g - particles[i])
            particles[i] += t * v[i]
        p = getP(func, particles, p)
        newG = getG(func, particles, g)
        if func(newG) < func(g):
            g = newG
        print('Оптимальная точка на текущей итерации:', g)
        print('Зачение в этой точке:', func(g))

    print('Оптимальная точка:', g)
    print('Зачение в этой точке:', func(g))


def f(x):
    x1 = x[0]
    x2 = x[1]
    return 3 * x1 * x1 + x1 * x2 + 3 * x2 * x2 - 8 * x1


solve(f, 10, [[-5, 5], [-5, 5]], 3, 30)

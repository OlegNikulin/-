import random
S = 10
n = 2
m = 1
N = 5
M = 2
distance = 10


def getDistance(p1, p2):
    s = 0
    for i in range(len(p1)):
        s += (p1[i] - p2[i]) ** 2
    return s ** 0.5


def getRandomPoint(x, distance):
    res = [
        x[i] + random.random() * distance - distance / 2
        for i in range(len(x))
    ]
    while getDistance(x, res) > distance:
        res = [
            x[i] + random.random() * distance - distance / 2
            for i in range(len(x))
        ]
    return res


def solve(func, limits, distance, delta, it):
    s = []
    for _ in range(S):
        s.append([
            (limits[i][1] - limits[i][0]) * random.random() + limits[i][0]
            for i in range(len(limits))
        ])
    f = [func(a) for a in s]
    checked = []
    s = sorted(s, key=func)
    d = []
    while len(checked) < len(s):
        maxS = None
        currentI = None
        for i in range(len(s)):
            for j in range(len(s)):
                if j not in checked:
                    maxS = s[j]
                    checked.append(j)
                    break
            if i not in checked:
                if getDistance(maxS, s[i]) < distance:
                    checked.append(i)
                    if func(maxS) > func(s[i]):
                        maxS = s[i]
            d.append(maxS)
        newAgents = []
        k = 0
        while k < it:
            newD = []
            k += 1
            print('\nИтерация', k)
            for i in range(n):
                agents = [d[i]]
                for _ in range(N):
                    agents.append(getRandomPoint(d[i], delta))
                agents = sorted(agents, key=func)
                newD.append(agents[0])

            for i in range(n, n + m):
                agents = [d[i]]
                for _ in range(M):
                    agents.append(getRandomPoint(d[i], delta))
                agents = sorted(agents, key=func)
                newD.append(agents[0])
            d = newD
            pMin = min(d, key=func)

            print('Текущая оптимальная точка:', pMin)
            print('Значение функции в этой точке:', func(pMin))
        pMin = min(d, key=func)
        print('\nОптимальная точка:', pMin)
        print('Значение функции в этой точке:', func(pMin))


def f(x):
    x1 = x[0]
    x2 = x[1]
    return 3 * x1 * x1 + x1 * x2 + 3 * x2 * x2 - 8 * x1


solve(f, [[-5, 5], [-5, 5]], 2, 2, 20)

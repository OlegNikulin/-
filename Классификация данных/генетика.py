import random


def f(x):
    x1 = x[0]
    x2 = x[1]
    return 3 * x1 * x1 + x1 * x2 + 3 * x2 * x2 - 8 * x1


def getRandomPoints(count, limits):
    res = []
    for _ in range(count):
        res.append([
            (limits[i][1] - limits[i][0]) * random.random() + limits[i][0]
            for i in range(len(limits))
        ])
    return res


def crossover(x1, x2):
    return [(x1[i] + x2[i]) / 2 for i in range(len(x1))]


def mutate(x, d):
    return [
        d * random.random() + x[i] - d / 2
        for i in range(len(x))
    ]


def solve(func, count, selectedCount, mutationDelta, limits, iters):
    points = getRandomPoints(count, limits)
    absMin = None
    for it in range(iters):
        print('Итерация', it)
        f = [func(x) for x in points]
        n = sorted(list(range(count)), key=lambda x: f[x])
        a = random.random() + 1
        b = 2 - a
        fMin = min(f)
        fSum = sum(f)
        adoptation = [
            -(f[i] - fMin + 0.1)
            for i in range(count)
        ]
        adoptation = [
            1 / count * (a - (a - b) * (n.index(i) - 1) / (count - 1))
            for i in range(count)
        ]
        s = []
        while len(s) < selectedCount:
            i = random.choices(
                list(range(len(points))),
                weights=adoptation)[0]
            s.append(points[i])
            points.pop(i)
            adoptation.pop(i)

            parents = []
        for _ in range(int(len(s) // 2)):
            parents.append(random.sample(s, 2))
        for pair in parents:
            s.append(crossover(pair[0], pair[1]))

        while len(s) < count:
            s.append(mutate(random.choice(s), mutationDelta))

        points = s

        optimal = min(s, key=func)
        if absMin is None:
            absMin = optimal
        elif func(optimal) < func(absMin):
            absMin = optimal
        print('Текущая минимальная точка:', absMin)
        print('Значение функции в этой точке:', func(absMin))

    print('Оптимальная точка:', absMin)
    print('Значение функции в этой точке:', func(absMin))


solve(f, 20, 6, 3, [[-10, 10], [-10, 10]], 20)

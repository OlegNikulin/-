from numpy import array
from math import sqrt


def changer(t, tx):
    n = 0.6
    a = []
    for i1 in range(len(tx)):
        a.append(tx[i1] - t[i1])
    a = array(a)
    a = n * a
    for i1 in range(len(t)):
        t[i1] += a[i1]
        t[i1] = round(t[i1], 3)
    return t


def kox():
    global W
    d1 = 0
    d2 = 0

    for j in range(len(X)):
        d1 += (X[j] - W[0][j]) ** 2
        d2 += (X[j] - W[1][j]) ** 2

    d1 = sqrt(d1)
    d2 = sqrt(d2)
    print("Старые веса слоя Кохонена", W)
    if d1 < d2:
        W[0] = changer(W[0], X)
        return [1, 0]

    else:
        W[1] = changer(W[1], X)
        return [0, 1]


def gro(k1):
    d1 = 0
    d2 = 0
    for i1 in range(len(k1)):
        d1 += round(k1[i1] * V[0][i1], 4)
        d2 += round(k1[i1] * V[1][i1], 4)
    return [d1, d2]


if __name__ == '__main__':
    X = [1, 0, 1, 0]
    W = [[0.2, 0.6, 0.5, 0.9], [0.8, 0.4, 0.7, 0.3]]
    Y = [0, 1]
    V = [[0.3, 0.7], [0.1, 0.8]]

    for l1 in range(5):
        k = kox()
        print("Вывод слоя Кохонена", k)
        g = gro(k)
        print("Новые веса слоя Кохонена", W)
        print("Вывод слоя Гроссберга", g)
        print('Старые веса для нейронов Гроссберга:', V)
        if k[0] == 1:
            V[0][0] = round(V[0][0] + 0.6 * (Y[0] - V[0][0]), 4)
            V[1][0] = round(V[1][0] + 0.6 * (Y[0] - V[1][0]), 4)
        else:
            V[0][1] = round(V[0][1] + 0.6 * (Y[1] - V[0][1]), 4)
            V[1][1] = round(V[1][1] + 0.6 * (Y[1] - V[1][1]), 4)
        print('Новые веса для нейронов Гроссберга:', V)
        print()

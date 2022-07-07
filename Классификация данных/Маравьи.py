
import random

alpha = 3
beta = 1
p = 0.1
q = 10


def getRandomCities(n, xLim=100, yLim=100):
    res = []
    for _ in range(n):
        res.append([
            random.random() * xLim,
            random.random() * yLim
        ])
    return res


class Ant(object):
    def __init__(self, cityIndex, edges):
        self.currentCity = cityIndex
        self.visited = [self.currentCity]
        self.edges = edges
        self.newFerm = 0

    def move(self):
        notVisited = []
        for i in range(len(self.edges)):
            if i not in self.visited:
                notVisited.append(i)

        if len(notVisited) == 0:
            print('len(notVisited) is 0!')
            return
        probabilities = []
        tn = []
        for i in notVisited:
            tn.append(self.edges[self.currentCity][i].ferment ** alpha +
                      1 / self.edges[self.currentCity][i].length)
        tnSum = sum(tn)
        if tnSum == 0:
            self.currentCity = random.choice(notVisited)
        else:
            for i in range(len(notVisited)):
                probabilities.append(tn[i] / sum(tn))
            self.currentCity = random.choices(notVisited,
                                              weights=probabilities)[0]
        self.visited.append(self.currentCity)

    def endIteration(self):
        length = 0
        for i in range(1, len(self.visited)):
            length += self.edges[self.visited[i - 1]][self.visited[i]].length
        self.newFerm = q / length
        for i in range(1, len(self.visited)):
            self.edges[self.visited[i - 1]][self.visited[i]].ferment += (
                    p * self.newFerm)
        self.visited = [self.currentCity]


class Edge(object):
    def __init__(self, city1, city2=None):
        if city2 is None:
            self.length = city1
        else:
            self.length = ((city1[0] - city2[0]) ** 2 +
                           (city1[1] - city2[1]) ** 2) ** 0.5
        self.ferment = 0


def printMatrix(m):
    s = ''
    for line in m:
        for a in line:
            s += str(a) + '\t'
        s += '\n'
    print(s[:-1])


def getOptimalPath(edges):
    path = [[0, max([[i, edges[0][i].ferment]
                     for i in range(len(edges))],
                    key=lambda x: x[1])[0]]]
    visited = [0, path[0][1]]
    while len(path) < len(edges):
        m = -1
        index = -1
        for i in range(len(edges[path[-1][1]])):
            if (m < edges[path[-1][1]][i].ferment
                    and (i not in visited or
                         (len(visited) == len(edges) and i == 0))):
                index = i
                m = edges[path[-1][1]][i].ferment
        path.append([path[-1][1], index])
        visited.append(index)
    return path


def getPathDistance(path, edges):
    return sum([edges[p[0]][p[1]].length for p in path])


def solveByEdges(edges, it, out=0):
    print('Длины путей:')
    printMatrix([[e.length for e in line] for line in edges])

    ants = []
    for i in range(len(edges)):
        ants.append(Ant(i, edges))

    for i in range(it):
        if out > 0:
            print('\nИтерация:', i)
        for _ in range(len(edges) - 1):
            for a in ants:
                a.move()
        for a in ants:
            a.endIteration()
        for line in edges:
            for e in line:
                e.ferment *= (1 - p)
        path = getOptimalPath(edges)
        if out > 1:
            print('Путь:', path)
        if out > 0:
            print('Длина пути:', getPathDistance(path, edges))

    printMatrix([[format(e.ferment, '0.3f')
                  for e in line]
                 for line in edges])
    path = getOptimalPath(edges)
    print('Оптимальный путь:', path)
    print('Дистанция:', getPathDistance(path, edges))


def solveByCities(cities, it, out=0):
    edges = []
    for i in range(len(cities)):
        edges.append([])
        for j in range(len(cities)):
            edges[i].append(Edge(cities[i], cities[j]))
    return solveByEdges(edges, it, out)


solveByCities(getRandomCities(30), 50)

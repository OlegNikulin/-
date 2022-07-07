from math import sqrt
from random import randint

n = int(input("Введите количество клиентов: "))
m = int(input("Введите количество объектов: "))
table1 = [[randint(1, 10) for j in range(m)] for i in range(n)]
print("Бинарная таблица клиентов и объектов: " + '\n' + '  ')
for s in range(m):
    print("  O", s + 1, sep='', end=' ')
print()
for list1 in range(len(table1)):
    print("К", list1, sep='', end=' ')
    for a1 in range(len(table1[list1])):
        if table1[list1][a1] == 10:
            print(table1[list1][a1], end='   ')
        else:
            print(table1[list1][a1], end='    ')
    print()
print()

while True:
    x, y = [int(s) - 1 for s in input("Введите номера оценок:").split()]
    k1, k2 = [int(s) - 1 for s in input("Введите номера клиентов:").split()]
    a = []
    b = []
    a.append(table1[k1][x])
    a.append(table1[k1][y])
    b.append(table1[k2][x])
    b.append(table1[k2][y])
    res = (a[0] - b[0])**2 + (a[1] - b[1])**2
    print("Сходство по L2 норме =", sqrt(res))
    r = int(input("Введите 1 чтобы завершить, лил любое другое число, чтобы продолжить: "))
    if r == '1':
        break

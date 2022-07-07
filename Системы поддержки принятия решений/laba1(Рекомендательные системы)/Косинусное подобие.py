from random import randint
from math import sqrt
n = int(input("Введите количество документов: "))
m = int(input("Введите количество частотных векторов: "))
table1 = [[randint(0, 5) for j in range(m)] for i in range(n)]
print("Бинарная таблица документов и частотных векторов: " + '\n' + '  ')
for s in range(m):
    print("  В", s + 1, sep='', end=' ')
print()
for list1 in range(len(table1)):
    print("Д", list1, sep='', end=' ')
    for a1 in range(len(table1[list1])):
        if table1[list1][a1] == 10:
            print(table1[list1][a1], end='   ')
        else:
            print(table1[list1][a1], end='    ')
    print()
print()
while True:
    a, b = [int(s) - 1 for s in input("Введите через пробел номера сравниваемых документов: ").split()]
    res1 = 0
    res2 = 0
    mul = 0
    for i in range(m):
        mul += table1[a][i] + table1[b][i]
        res1 += table1[a][i] ** 2
        res2 += table1[b][i] ** 2

    res1 = sqrt(res1)
    res2 = sqrt(res2)
    sim = round(mul / (res1 * res2), 3)
    if sim == 0:
        print("Зависимость междупредпочтениями пользователей не просматривается")
    elif 0 < sim <= 0.5:
        print("Слабая зависмость равная:", sim)
    else:
        print("Сильная зависимость равная:", sim)

    r = int(input("Введите 1 чтобы завершить, лил любое другое число, чтобы продолжить: "))
    if r == '1':
        break

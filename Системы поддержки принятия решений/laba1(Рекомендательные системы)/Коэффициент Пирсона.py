from random import randint
from math import sqrt
n = int(input("Введите количество пользователей: "))
m = int(input("Введите количество оценок: "))
table1 = [[randint(0, 5) for j in range(m)] for i in range(n)]
print("Бинарная таблица документов и частотных векторов: " + '\n' + '  ')
for s in range(m):
    print("  О", s + 1, sep='', end=' ')
print()
for list1 in range(len(table1)):
    print("П", list1, sep='', end=' ')
    for a1 in range(len(table1[list1])):
        if table1[list1][a1] == 10:
            print(table1[list1][a1], end='   ')
        else:
            print(table1[list1][a1], end='    ')
    print()
print()

while True:
    average1 = 0
    average2 = 0
    x, y = [int(s) for s in input("Введите номера пользователей: ").split()]
    for i in range(m):
        average1 += table1[x][i]
        average2 += table1[y][i]
    average1 = round(average1 / m, 3)
    average2 = round(average2 / m, 3)
    print("Среднее арифметическое оценок для пользователя", x, '=', average1)
    print("Среднее арифметическое оценок для пользователя", y, '=', average2)
    user1 = []
    user2 = []
    for i in range(m):
        user1.append(round(table1[x][i] - average1, 3))
        user2.append(round(table1[y][i] - average2, 3))
    print("\nНовая таблица отклонения от среднего арифмитического:")
    print(user1)
    print(user2)
    numerator = 0
    den1 = 0
    den2 = 0
    for i in range(m):
        numerator += user1[i] * user2[i]
        den1 += user1[i] ** 2
        den2 += user2[i] ** 2
    den1 = sqrt(den1)
    den2 = sqrt(den2)
    sim = numerator / (den1 * den2)
    print("Коэффициент корреляции =", sim)
    if sim <= -0.5:
        print("Вкусы данных пользователей расходятся")
    elif sim >= 0.5:
        print("Вкеусы данных пользователей похожи")
    else:
        print("Линейной корреляции нет")
    op = input("Введите 1, чтобы завершить выполнение программы, любое другое значение, чтобы продолжить выполнение: ")
    if op == '1':
        break

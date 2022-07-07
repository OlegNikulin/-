from random import randint
n = int(input("Введите количество сторок пользователей: "))
m = int(input("Введите количество элементов: "))
table1 = [[randint(0, 1) for j in range(m)] for i in range(n)]
print("Бинарная таблица пользователей и элементов: " + '\n' + '  ')
for s in range(m):
    print("  O", s+1, sep='', end=' ')
print()
for list1 in range(len(table1)):
    print("П", list1, sep='', end=' ')
    for a1 in range(len(table1[list1])):
        print(table1[list1][a1], end='    ')
    print()
print()
while True:
    s = input("\nВведите: 1-если хотите выбрать покупателей, 2-для элементов, 3-для выхода: ")
    if s == '1':
        a, b = [int(s1) - 1 for s1 in input("Введите через пробел номера покупателй для сравнения:").split()]
        users1 = []
        users2 = []
        for i in range(m):
            users1.append(table1[a][i])
            users2.append(table1[b][i])
        print("Таблица выбранных покупателей и соответствующих им элементов:" + '\n')
        print(users1)
        print(users2)
        count = 0
        for i1 in range(len(users1)):
            if users1[i1] == users2[i1]:
                count += 1
        print("Количество одиноковых элементов =", count)
        print("Количество всех элементов=", len(users1))
        print("\nСходство Жакара между пользователем", a, "и пользователем", b, "=", count / len(users1))
    elif s == '2':
        a, b = [int(s2)-1 for s2 in input("Введите через пробел номера элементов для сравнения:").split()]
        elem1 = []
        elem2 = []
        for i in range(n):
            elem1.append(table1[i][a])
            elem2.append(table1[i][b])
        print("Таблица выбранных элементов и связанных с ними пользователей\n")
        count = 0
        for i in range(n):
            print(elem1[i], elem2[i])
            if elem1[i] == elem2[i]:
                count += 1
        print("\nКоличество одиноковых элементов =", count)
        print("Количество всех элементов=", len(elem1))
        print("\nСходство Жакара между элементом", a, "и элементом", b, "=", count / len(elem1))
    elif s == '3':
        break
    else:
        print("Введено неверное значение!")

from math import sqrt


# Функции для 3-го шага

def cel_func(x, y):
    return (x**2) - (x*y) +3*(y**2) - x


def maximus():
    global max1, op
    for a, b in list1:
        max1.append(cel_func(a, b))
    max2 = max1[0]
    op.append(list1[0])
    if max1[0] < max1[1] > max1[2]:
        max2 = max1[1]
        op.pop(0)
        op.append(list1[1])
        list1.pop(1)
    elif max1[0] < max1[2] > max1[1]:
        max2 = max1[2]
        op.pop(0)
        op.append(list1[2])
        list1.pop(2)
    else:
        list1.pop(0)
    return max2


# Функция для 4-го шага

def center_of_gravity(a):
    global xc
    sum1 = 0
    sum2 = 0
    for x, y in a:
        sum1 += x
        sum2 += y
    xc = [sum1 / 2, sum2 / 2]


# Функция для 5-го шага

def reflection():
    global xc, x3
    xc[0] = xc[0] * 2
    xc[1] = xc[1] * 2
    x3.append(xc[0] - op[0][0])
    x3.append(xc[1] - op[0][1])


# Функция для 6-го шага

def check():
    global flag, list1
    if cel_func(op[0][0], op[0][1]) > cel_func(x3[0], x3[1]):
        flag = True
        list1.append(x3)
    else:
        list1.append(x3)
        flag = False


#  Функция для выполнения 7-го шага

def Reduction():
    global list1, min1
    list3 = [cel_func(i, j) for i, j in list1]
    if list3[1] > list3[0] < list3[2]:
        min1 = list1[0]
    elif list3[0] > list3[1] < list3[2]:
        min1 = list1[1]
    elif list3[0] > list3[2] < list3[1]:
        min1 = list1[2]
    b = 0
    for i, j in list1:
        x = [min1[0] + 0.5 * (i - min1[0]), min1[1] + 0.5 * (j - min1[1])]
        del list1[b]
        list1.insert(b, x)
        b += 1
    print(list1)


# Функция для 8-го шага

def simplex_center():
    global coord, xc8
    sum1 = 0
    sum2 = 0
    for a, b in list1:
        sum1 += a
        sum2 += b
    coord.append(sum1 / 3)
    coord.append(sum2 / 3)
    xc8 = cel_func(coord[0], coord[1])


# 9 шаг -  проверка условия окончания процесса вычислений

def main_checker():
    global list2, flag1, max1, min1, op, xc, x3, flag, coord, xc8, counter1
    x_new1 = []
    for a, b in list1:
        list2.append(cel_func(a, b) - xc8)
        x_new1.append(cel_func(a, b))
    print("Значения для проверки", list2)
    for i in list2:
        if i > e:
            print("Условия окончания поиска не выполняются, процесс итераций должен быть продолжен.")
            max1 = []
            min1 = []
            op = []
            xc = []
            x3 = []
            coord = []
            xc8 = 0
            flag = True
            list2 = []
            counter1+=1
            print("--------------------------------------------------------------------")
            break
    else:
        print("Все условия окончания поиска выполняются - процесс итерации завершен!")
        print("Наименьшее значение функции =", min(x_new1))
        flag1 = False


# 1 шаг - задать точность, длину ребра симплекса, размерность задачи, начальную точку симплекса"

e = float(input("Задайте точность: "))
m = float(input("Задайте  длину ребра симплекса: "))
n = int(input("Задайте размерность задачи оптимизации: "))
x0 = [int(input("Первая координата точки: ")), int(input("Вторая координата точки: "))]
max1 = []  # список значений целевой функции в точках
min1 = []  # точка минимума
op = []  # точка с наибольшим значением целевой функции
xc = []  # точка - центр тяжести
x3 = []  # отраженная точка
flag = True  # проверка условия на 6-ом шаге
coord = []  # координаты центра тяжести симплекса
xc8 = 0  # значение функции в центре тяжести симплекса
flag1 = True  # проверка условия прекращения работы алгоритма
list2 = []  # значения для проверки условия окончания работы алгоритма
counter1 = 0  # глобальный счетчик для выполнения итераций

# 2 шаг - вычислить координаты остальных n вершин симплекса

del1 = ((sqrt(n + 1) - 1) / (n * sqrt(2))) * m
del2 = ((sqrt(n + 1) + (n - 1)) / (n * sqrt(2))) * m
print(round(del1, 3), round(del2, 3))
x1 = [x0[0] + del1, x0[1] + del2]
x2 = [x0[0] + del2, x0[0] + del1]
list1 = [x0, x1, x2]  # список вершин
counter = 0
for i in list1:
    print("Точка", counter, i)
    counter += 1
while flag1:
    print("Интерация", counter1)

    # 3 шаг - Определить номер вершины с наибольшим значением целевой функции
    print("Максимальное значение целевой функции", maximus(), "\n" + "В точке:", op[0])
    counter = 0
    print("Остальные точки")
    for i in list1:
        print("Точка - ", i, '- значение целевой функции в точке', max1[counter])
        counter += 1

    #  4 шаг - определяем центр тяжести всех вершин за исключением найденного максимума

    center_of_gravity(list1)
    print("Центр тяжести расположен в точке:", xc)

    # 5 шаг -  отражаем вершину максимума относительно центра тяжести
    # вычисляем значение целевой функции в отраженной точке

    reflection()
    print("Координаты отраженной вершины:", x3)

    # 6 шаг проверка успешности операции отражения

    check()

    if flag:

        # 8 шаг - определение центра тяжести симплекса
        # значение функции в этой точке
        print("Наблюдается уменьшение целевой функции")
        simplex_center()
        print("Точка центра тяжести симплекса:", coord)

    else:

        # 7 шаг выполнение операции редукции

        print("Выполнение операции редукции")
        Reduction()

        # 8 шаг - определение центра тяжести симплекса
        # значение функции в этой точке

        simplex_center()
        print("Точка центра тяжести симплекса:", coord)

    main_checker()
    print(list1)

from math import sqrt

e = float(input("Задайте точность:"))  # - точность
n = int(input("Задайте размерность задачи: "))  # размерность задачи оптимизации
starting_point = [int(input("Введите первую координату начальной точки: ")), int(input("Введите вторую координату: "))]
m = float(input("Введите размер ребра симплекса: "))
b = float(input("Введите парметр растяжения: "))
y = float(input("Введите параметр сжатия"))
#  Вычисляем приращение
delta1 = ((sqrt(n + 1) - 1) / (n * sqrt(2))) * m
delta2 = ((sqrt(n + 1) - 1 + n) / (n * sqrt(2))) * m
global_counter = 0
point1 = [starting_point[0] + delta1, starting_point[1] + delta2]
point2 = [starting_point[0] + delta2, starting_point[1] + delta1]


def cel_func(x, super):
    return (x ** 2) - (x * super) + 3 * (super ** 2) - x


def maximus():
    global max1, op
    for a, b_super in list1:
        max1.append(cel_func(a, b_super))
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


def reflection():
    global xc, x3
    xc[0] = xc[0] * 2
    xc[1] = xc[1] * 2
    x3.append(xc[0] - op[0][0])
    x3.append(xc[1] - op[0][1])


def final_checker():
    global xc, global_counter, flag
    xc = [(1 / 3) * (list1[0][0] + list1[1][0] + list1[2][0]), (1 / 3) * (list1[0][1] + list1[1][1] + list1[2][1])]
    print('В полученной точке центра тяжести симплекса,  функция = ', cel_func(xc[0], xc[1]))
    puf1 = cel_func(xc[0], xc[1])
    final_list = []
    for a, b_super in list1:
        final_list.append(cel_func(a, b_super))
    gur = (1 / (n + 1))
    sigma = (gur * ((final_list[0] - puf1) ** 2 + (final_list[1] - puf1) ** 2 + (final_list[2] - puf1) ** 2))**(1/2)
    print("Значение сигмы: ", sigma)
    if e>sigma:
        print("Поиск алгоритма закончен")
        print("Минимальное значение целевой функции:", min(final_list))
        flag= False
    else:
        print("Условие окончания поиска не выполнено!")
        global_counter+=1
        print("_____________________________________________________________________________")


def minimum_points():
    global min_values
    minimum_list = []
    for i1, j1 in list1:
        minimum_list.append(cel_func(i1, j1))
    if minimum_list[1]>minimum_list[0]:
        min_values = list1[0]
        list1.pop(0)
    elif minimum_list[0]>minimum_list[1]:
        min_values = list1[1]
        list1.pop(1)


def reductions():
    global x4, x5, list1
    minimum_points()
    x4 = [min_values[0] + 0.5 * (op[0][0] - min_values[0]), min_values[1] + 0.5 * (op[0][1] - min_values[1])]
    x5 = [min_values[0] + 0.5 * (list1[0][0] - min_values[0]), min_values[1] + 0.5 * (list1[0][1] - min_values[1])]
    list1.clear()
    list1.append(min_values)
    list1.append(x4)
    list1.append(x5)
    print("Новый многогранник образован следующими вершинами и соответствующими значениями целевой функции")
    for r, t in list1:
        print(r, t, '=', cel_func(r, t))


def compression():
    global x4, list1, xr, fxr
    if fs < meaning_new_point < fh:
        print("Условие выполнено выполняется операция сжатия симплекса")
        x4 = [xc[0] + y * (x3[0] - xc[0]), xc[1] + y * (x3[1] - xc[1])]
        print("В полученной вершине значение целевой функции =", cel_func(x4[0], x4[1]))
        if cel_func(x4[0], x4[1]) < meaning_new_point:
            print("Операция сжатия закончилась удачно")
            list1.append(x4)
            print("Следовательно текущий симплекс образован вершинами", list1)
            xr = x4
            fxr = cel_func(xr[0], xr[1])
            final_checker()
            print(list1)
        else:
            reductions()
            final_checker()
    else:
        reductions()
        final_checker()


list1 = [starting_point, point1, point2]  # список вершин
meaning_cel = []  # список значений функции
for i, j in list1:
    meaning_cel.append(cel_func(i, j))
flag = True
while flag:
    min_values = []
    print("итерация №", global_counter)
    op = []  # точка с наибольшим значением целевой функции
    max1 = []  # список значений целевой функции в точках
    x3 = []  # отраженная точка
    maximus()
    fh = max(max1)
    max1.remove(fh)
    xr = op
    fxr = fh
    fj = min(max1)
    max1.remove(fj)
    fs = max1[0]
    x4 = ''
    x5 = ''
    print("Наибольшее значение целевой функции соответствует вершине: ", op[0])
    xc = [(list1[0][0] + list1[1][0]) / 2, (list1[0][1] + list1[1][1]) / 2]
    print("Центр тяжести расположен в точке", xc)
    print(list1)
    reflection()
    print("Координаты отраженной вершины:", x3)
    xc = [(list1[0][0] + list1[1][0]) / 2, (list1[0][1] + list1[1][1]) / 2]
    meaning_new_point = cel_func(x3[0], x3[1])
    print("В полученной вершине значение целевой функции:", meaning_new_point)
    if meaning_new_point < cel_func(op[0][0], op[0][1]):
        print("Наблюдается уменьшение целевой функции")
        xr = x3
        fxr = meaning_new_point
        if fxr<fj:
            print("Выполняется операция растяжения")
            x3 = [xc[0] + b*(xr[0] - xc[0]), xc[1] + b*(xr[1] - xc[1])]
            fx3 = [cel_func(x3[0], x3[1])]
            print("Значение целевой функции", fx3)
            if fx3<fxr:
                print("Операция растяжения закончилась успешно!")
                final_checker()
            else:
                compression()
        else:
            compression()
    else:
        compression()

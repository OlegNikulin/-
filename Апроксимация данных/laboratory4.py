from math import sqrt


def cel_func(x, y):
    return (x**2) - (x*y) +3*(y**2) - x


def grad(x, y):
    return [2*x - y - 1, -1 *x + 6*y]


def new_start():
    global grad1, norm, flag
    grad1 = grad(x0[0], x0[1])
    norm = sqrt((grad1[0] ** 2) + (grad1[1] ** 2))
    print("Значение нормы =", round(norm, 3))


flag = True
x0 = [0, 0]
e = 0.1
h = 0.4
k = 0
norm = 0
grad1 = []
print("Итерация", k)
new_start()
if norm <= e:
    print("Расчет окончен")
    x0 = [round(v, 3) for v in x0]
    print("Минимальная точка", x0)
    print("Минимальное значение в точке", round(cel_func(x0[0], x0[1]), 3))
else:
    while True:
        grad2 = grad(x0[0], x0[1])
        x1 = [x0[0] - h * grad2[0], x0[1] - h * grad2[1]]
        x1 = [round(v, 3) for v in x1]
        print("Новая точка", x1)
        print("Значение функции в новой точке", round(cel_func(x1[0], x1[1]), 3))
        if cel_func(x1[0], x1[1]) < cel_func(x0[0], x0[1]):
            print("Условия убывания функции выполнены")
            k += 1
            x0 = x1[:]
            new_start()
            if norm <= e:
                print("Расчет окончен")
                x0 = [round(v, 3) for v in x0]
                print("Минимальная точка", x0)
                print("Минимальное значение в точке", round(cel_func(x0[0], x0[1]), 3))
                break
            print("Условия окончания поиска не выполнены, итерации продалжаются ")
            print("Итерация", k)
        elif cel_func(x1[0], x1[1]) > cel_func(x0[0], x0[1]):
            print("Условия убывания функции не выполнены, уменьшаем шаг и ищем новую точку")
            h /= 2

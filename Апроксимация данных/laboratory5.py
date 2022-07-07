from math import sqrt

from sympy import symbols, diff, solve

esp = 0.1
x0 = [0, 0]
n = 2
k = 0
h0 = symbols('h0')
flag = True


def cel(x1, x2):
    return x1**2 - x1*x2 + 3*x2**2 -x1


def grad(x1, x2):
    return [2*x1 - x2 - 1, -1*x1 + 6*x2]


def formula_coord(x1, x2):
    xgrad = grad(x1, x2)
    x1 = [x1 - h0*xgrad[0], x2 - h0*xgrad[1]]
    rez = solve(diff(cel(x1[0], x1[1]), h0), h0)
    return rez[0].n(5)


while True:
    print("Итерация", k)
    h1 = formula_coord(x0[0], x0[1])
    print("Текущее значение шага", h1)
    print("Старая точка", x0)
    x0grad = grad(x0[0], x0[1])
    x1 = [x0[0] - h1*x0grad[0], x0[1] - h1*x0grad[1]]
    print("Новая точка:", x1)
    x1grad = grad(x1[0], x1[1])
    xnorma = sqrt(x1grad[0]**2 + x1grad[1]**2)

    if xnorma <= esp:
        print("Точка минимума", x1)
        print("Минимальное значение:", cel(x1[0], x1[1]))
        break
    elif xnorma>esp:
        print("Условие окончание не выполнено!")
        x0 = x1[:]
        k+=1

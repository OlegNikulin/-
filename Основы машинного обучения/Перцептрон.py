def func_active(s1):
    if s1 > 0:
        return 1
    else:
        return -1


if __name__ == '__main__':
    x = [[1, 1, 1],
         [1, -1, -1],
         [-1, 1, -1],
         [-1, -1, -1]]

    n = 1
    e_set, w11, w21, T, k = [0 for i in range(5)]
    flag = True

    while flag:
        for t in range(4):
            print("Итерация: ", k)
            s = x[t][0] * w11 + x[t][1] * w21 + -1 * T
            print('NET =', s)
            y = func_active(s)
            print('y =', y, 'Ожидалось =', x[t][2])
            if y == x[t][2]:
                e = 0
                print("Ошибка е =", e)
                print("Оптимальные для работы персептрона веса =", w11, w21, T)
                flag = False
                break
            else:
                e = x[t][2] - y
                print("Ошибка е =", e)
                w11 = w11 + n * e * x[t][0]
                w21 = w21 + n * e * x[t][1]
                T = T + n * e * -1
                print("Новые веса:", w11, w21, T)
                k += 1
                print()

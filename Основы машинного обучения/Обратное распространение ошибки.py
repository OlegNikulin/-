from math import exp


def activate(W1, W2, U11, U22, W00, X00=1):
    NET = W1*U11 + W2*U22 + W00*X00
    return round(1/(1 + exp(-1*NET)), 5)


def step23():
    U33 = activate(W31, W32, U1, U2, W03)
    U44 = activate(W41, W42, U1, U2, W04)
    print("Скрытый слой: ", U33, U44)
    U55 = activate(W53, W54, U33, U44, W05)
    print("Выходной слой:", U55)
    e1 = round(0.5 * (1 - U55) ** 2, 6)
    print("Ошибка =", e1)
    return U33, U44, U55, e1


def step4():
    sig55 = round(U5*(1-U5)*(d-U5), 7)
    print("Ошибка в выходном узле:", sig55)
    sig33 = round(U3*(1-U3)*(W53*sig55), 7)
    sig44 = round(U4*(1-U4)*(W54*sig55), 7)
    print("Ошибки скрытых слоев:", sig33, sig44)
    return sig55, sig33, sig44


def step5():
    U00 = 1
    U = [[U4, U3, U00], [U2, U1, U00], [U2, U1, U00]]
    sig = [sig5, sig4, sig3]
    W = [[W54, W53, W05], [W42, W41, W04], [W32, W31, W03]]
    for i in range(3):
        for j in range(3):
            W[i][j] = round(W[i][j] + a*sig[i]*U[i][j], 6)
    return W


if __name__ == '__main__':
    
    print("Движение вперёд\n")
    U1, U2, d, a = 0, 1, 1, 0.5
    print("Входной слой:", U1, U2)
    W03, W04, W05 = [1 for i in range(3)]
    W31, W32, W41, W42 = 1, 0.5, -1, 2
    W53, W54 = 1.5, -1.0
    U3, U4, U5, e = step23()
    print("\nОбратный проход\n")
    sig5, sig3, sig4 = step4()
    WW = step5()
    WW0 = [[W54, W53, W05], [W42, W41, W04], [W32, W31, W03]]
    U0 = [U3, U4, U5]
    print("Новые веса", WW)
    W54, W53, W05 = [WW[0][j] for j in range(3)]
    W42, W41, W04 = [WW[1][j] for j in range(3)]
    W32, W31, W03 = [WW[2][j] for j in range(3)]
    print("\nПроверка\n")
    U3, U4, U5, e2 = step23()
    if e2 < e:
        print("Текущая ошибка меньше предыдущей на", round(e - e2, 6))
    else:
        print("Данное решение не привело к уменьшению ошибки!")

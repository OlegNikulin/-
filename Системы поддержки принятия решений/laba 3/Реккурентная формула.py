import numpy as np
print("Матрица вероятностей перехода:\n")
P = np.array([[0.8, 0.2], [0.9, 0.1]])
print(P)

print("\nВектор начальных вероятностей:\n")
P0 = np.array([0.0, 1.0])
print(P0, '\n')

k = int(input("Введите номер шага: "))
for i in range(k):
    Pk1 = round(P0[0] * P[0, 0] + P0[1] * P[1, 0], 3)
    Pk2 = round(P0[0] * P[0, 1] + P0[1] * P[1, 1], 3)
    P0[0] = Pk1
    P0[1] = Pk2
    print("P1 =", P0[0], "P2 =", P0[1])

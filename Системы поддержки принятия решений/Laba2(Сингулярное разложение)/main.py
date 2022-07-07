import numpy as np
from math import sqrt
A = np.array([[1, 0, 0, 1], [0, 1, 0, 1], [1, 0, 1, 1]])
AT = np.transpose(A)

print("\nИсходная матрица:\n", A)
print("\nТранспонированная матрица:\n", AT)

ATA = AT.dot(A)
print("\nМатрица АТА:\n", ATA)
w, v = np.linalg.eig(ATA)
print("\nСобственные числа:\n", w)
w2 = list(w)
for i in range(len(w2)):
    w2[i]= round(w2[i], 3)
    w2[i] = sqrt(w2[i])
    if w2[i] == -0.0:
        w2[i] = 0
w2 = sorted(w2, reverse=True)
print("Корни, собственных значений сигма =", w2)
D = np.eye(len(ATA[0, :]))
for i in range(len(ATA[0, :])):
    D[i][i] = w2[i]
D1 = []
for i in range(len(D[:, 0])):
    summer=0
    list3 = []
    for j in range(len(D[0, :])):
        if D[i, j]==0:
            summer+=1
        list3.append(D[i, j])
    if summer != len(D[0, :]):
        D1.append(list3)
D1 = np.array(D1)
print("\nМатрица D =\n", D1)
e = []

for i in range(len(v[:, 0])):
    for j in range(len(v[0, :])):
        v[i, j] = round(v[i, j])

print("\nСобственные векторы:\n", v)
for i in range(len(v[:, 0])):
    sum1 = 0
    for j in range(len(v[0, :])):
        sum1+=v[j, i]**2
    sum1 = sqrt(sum1)
    e.append(round(1/sum1, 5))

print("\nE =", e)
v2 = np.eye(len(v[0, :]))
for i in range(len(v[:, 0])):
    for j in range(len(v[0, :])):
        v2[i, j] = v[i, j]*e[i]

V = np.transpose(v2)
print("\nМатрица V =\n", V)

count = len(list(set(w2)))
f = []
for i in range(len(w2)):
    if w2[i] == 0 or w2[i]==0.0:
        w2[i] = 1

for i in range(count):
    top = (1/w2[i]) * A * e[i]
    top = top.dot(v[:, i])
    f.append(top)
f = np.array(f)
print('\n', f)
U = np.transpose(f)
print("\n Матрица U =\n", U)
print("Искомое сингулярное разложение")
print("A =", U, D1, v2, sep='\n\n')
print()
k = int(input("Введите число скрытых факторов: "))
D2 = []
for i in range(k):
    tea = []
    for j in range(k):
        tea.append(D1[i, j])
    D2.append(tea)

F = np.array([D2])
print("Таблица сингулярных значений Dk:\n\n", F)
V2 = []
for i in range(k):
    tea = []
    for j in range(len(v2[0, :])):
        tea.append(v2[i, j])
    V2.append(tea)
V2 = np.array(V2)
print("\nМатрица Vk =\n\n", V2)
U2 = []
for i in range(len(U[:, 0])):
    tea = []
    for j in range(k):
        tea.append(U[i, j])
    U2.append(tea)
U2 = np.array(U2)
print("\nМатрица U2 =\n\n", U2)
A2 = []
for i in range(len(U2[:, 0])):
    tea = []
    travel = 0
    for j in range(len(V2[0, :])):
        travel = V2[:, j].dot(U2[i, :])
        tea.append(travel)
    A2.append(tea)
A2 = np.array(A2)
print("\nМатрица А2=\n\n", A2)

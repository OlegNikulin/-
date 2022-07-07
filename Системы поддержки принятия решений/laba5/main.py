import numpy as np
matrix = np.array([[120.0, 94.0, 164.0],
                   [85.0, 75.2, 92.0],
                   [145.0, 81.0, 120.0],
                   [78.0, 76.8, 86.0],
                   [70.0, 75.9, 104.0]])

matrix2 = np.array([[99.6, 80.6, 113.2],
                    [28.4, 10.9, 27.9]])

print("\nФинансовые показатели:\n\n", matrix, '\n', matrix2)
Z = []
for i in range(len(matrix[:, 0])):
    tea = []
    for j in range(len(matrix[0, :])):
        res = matrix[i, j] - matrix2[0, j]
        den = matrix2[1, j]
        res /= den
        res = round(res, 3)
        tea.append(res)
    Z.append(tea)
Z = np.array(Z)
print('\nНормированная матрица:\n\n', Z)

D0 = []
for i in range(len(Z[:, 0])):
    tea = []
    for j in range(len(Z[:, 0])):
        result = 0
        for k in range(len(Z[0, :])):
            result += (Z[i, k] - Z[j, k])**2
        tea.append(round(result, 3))
    D0.append(tea)
for i in range(len(D0)):
    for j in range(len(D0[i])):
        if i>j:
            D0[i][j] = 0
D0 = np.array(D0)
print("\nПервоначальная матрица расстояния:\n\n", D0)
mini = D0[0][1]
index_i = 0
index_j = 0
for i in range(len(D0)):
    for j in range(len(D0)):
        if D0[i][j]<mini and D0[i][j]!=0:
            mini, index_i, index_j = D0[i][j], i, j
print("\nМинимальное значение = ", mini, "Объекты:", index_i, "и", index_j)

lime = []
for i in range(len(D0)):
    if i!=index_i and i!=index_j:
        lime.append(i)
if index_i<index_j:
    min_index = index_i
else:
    min_index = index_j
lime.append(min_index)
lime.sort()
print(lime)

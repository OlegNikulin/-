import numpy as np
import copy

P = np.array([[0.7, 0.2, 0.1], [0.8, 0.1, 0.1], [0.8, 0.05, 0.15]])
print("\nМатрица вероятностей переходов: \n\n", P)
det = np.transpose(P)

for i in range(len(det[:, 0])):
    for j in range(len(det[0, :])):
        if j != i:
            det[i, j] += 1

det00 = round(np.linalg.det(det), 3)
print('\n Дельта: \n', det, '  = ', det00)

det1 = copy.deepcopy(det)
det2 = copy.deepcopy(det)
det3 = copy.deepcopy(det)

for i in range(len(det[:, 0])):
    for j in range(len(det[0, :])):
        if j == 0:
            det1[i, j] = 1
        elif j == 1:
            det2[i, j] = 1
        elif j == 2:
            det3[i, j] = 1

det11 = round(np.linalg.det(det1), 3)
det22 = round(np.linalg.det(det2), 3)
det33 = round(np.linalg.det(det3), 3)

print("\n Дельта1:\n", det1, '  = ', det11)
print("\n Дельта2:\n", det2, '  = ', det22)
print("\n Дельта3:\n", det3, '  = ', det33)

print('\nP1 =', round(det11/det00, 3))
print('\nP2 =', round(det22/det00, 3))
print('\nP3 =', round(det33/det00, 3))

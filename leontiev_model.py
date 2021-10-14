import numpy as np

A = [[0.12, 0.2, 0.3], [0.25, 0.35, 0.15], [0.33, 0, 0.45]]
Y = [[300], [150], [450]]

B = np.linalg.matrix_power(np.eye(3) - A, -1)
print('Матрица полных материальных затрат B равна:\n', B)
if B.min() >= 0:
    print('Матрица A продуктивна, т.к. в матрице B все элементы неотрицательны.')
else:
    print('Матрица A непродуктивна, т.к. в матрице B есть отрицательные элементы.')

X = B.dot(Y)
print('Вектор валового выпуска X:\n', X)

xx = np.zeros((np.array(A).shape[0], np.array(A).shape[1]), dtype=float)
for i in range(0, np.array(A).shape[0]):
    for j in range(0, np.array(A).shape[1]):
        xx[i, j] = A[i][j] * X[j]
print('Межотраслевые поставки продукции:\n', xx)

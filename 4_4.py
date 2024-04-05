import random
import numpy as np

n = 5

mas = np.eye(n, n)
mas = np.random.uniform(0, 10, size=(n, n))
print(f'\nМатрица:\n {mas}')

count = 0;
for i in range(n):
    ColumnSum = np.sum(mas[:, i])
    if (ColumnSum >= 1):
        while (ColumnSum >= 1):
            mas[count][i] = np.random.uniform(0, 0.1)
            ColumnSum = np.sum(mas[:, i])
            count += 1
            if count == n: count = 0
print(f'\nНовая матрица:\n {mas}')

det = np.linalg.det(mas)
print(f'\nОпределитель: {det}')

E = np.eye(n, n)
B = E - mas
print(f'\nМатрица B:\n {B}')

C = np.linalg.inv(B)
print(f'\nМатрица C:\n {C}')

Vector = np.arange(0, 5)
np.random.shuffle(Vector)
print(f'\nВектор: {Vector}')

X = np.dot(C, Vector)
print(f'\nВектор X: {X}')

A = np.array([[0.54, 0.25, 0.2 ],
              [0.3 , 0.17, 0.1 ],
              [0.08, 0.06, 0.09]])
Y = np.array([[30],
              [17],
              [10]])
X = np.linalg.solve(A, (np.eye(3) - A).dot(Y))
print(f'\n\nНовый вектор X по заданию 7:\n {X}')






'''
np.random.shuffle(m1)
for i in range(n):
    for j in range(n):
        mas[i][j] = round(random.uniform(0,9), 2)
        print(mas[i][j], end = " ")
    print()


RowSum = 0
count = 0
for i in range(n):
    for j in range(n):
        RowSum += mas[i][j]
    if (RowSum > 1):
        while (RowSum > 1):
            mas[i][count] = round(random.uniform(0,0.2), 2)
            count += 1
            RowSum = 0
            for j in range(n):
                RowSum += mas[i][j]
            if (count == n):
                count = 0
        count = 0

print('\nНовая матрица:')
for i in range(n):
    for j in range(n):
        print(mas[i][j], end = " ")
    print()

det = np.linalg.det(mas)
print(f'\nОпределитель: {det}')

E = []
for i in range(n):
    E.append([1]*n)

B = np.eye(n,n)

print(f'\nМатрица B:')
for i in range(n):
    for j in range(n):
        B[i][j] = round(E[i][j] - mas[i][j], 2)
        print(B[i][j], end = " ")
    print()


if (det != 0 ):
    C = np.linalg.inv(B)
    C2 = C

    print(f'\nМатрица C:')
    for i in range(n):
        for j in range(n):
            print(C[i][j], end=" ")
        print()

    VectorList = [round(random.uniform(0,50.9), 2) for i in range(n)]
    Vector = np.array(VectorList)
    print(f'\nВектор: {Vector}')

    X = np.dot(C2, Vector)
    print(f'\nВектор X:', end= " ")
    for i in range(n):
        print(X[i], end=" ")
else:
    print('\nОпределитель = 0!')

A = np.array([[0.54, 0.25, 0.2],
              [0.3, 0.17, 0.1],
              [0.08, 0.06, 0.09]])

Y = np.array([30, 17, 10])

X = np.linalg.solve(A - np.eye(3), Y)

print(f'\n\nНовый вектор X по заданию 7: {X}')

'''
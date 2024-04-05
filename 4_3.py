import random
import numpy as np

n = 10

m1 = np.arange(1, 11)
m2 = np.arange(1, 11)

np.random.shuffle(m1)
np.random.shuffle(m2)
print("m1:", m1)
print("m2:", m2)

m3 = np.setxor1d(m1, m2)
print("m3:", m3)

m1[(m1 % 3 == 0) | (m1 % 2 == 0)] = 1
print("Измененный m1:", m1)

matrix = np.concatenate((m1, m2)).reshape(4, 5)
print("Матрица:")
print(matrix)

matrix = np.delete(matrix, [0, 3], axis=1)
print("Матрица после удаления:")
print(matrix)

print("Транспонированная матрица:")
print(matrix.T)

'''
m1 = [0] * n
m2 = [0] * n

for i in range(n):
    m1[i] = random.randint(1,10)
    m2[i] = random.randint(1, 10)

m3 = []
for i in range(n):
    if (m1[i] not in m2):
        m3.append(m1[i])
    elif (m2[i] not in m1):
        m3.append(m2[i])

print(f'\nМассив m3: {m1}')
print(f'Массив m3: {m2}')
print(f'Массив m3: {m3}')

for i in range(n):
    if (m1[i]%3 == 0 or m1[i]%2 == 0):
        m1[i] = random.randint(1,10)
print(f'Новый массив m1: {m1}')

NewMas = []
for i in range(4):
    NewMas.append([0]*5)
count = 0

for i in range(4):
    for j in range(5):
        if (count < 10):
            NewMas[i][j] = m1[count]
        else:
            NewMas[i][j] = m2[count - 10]
        count += 1

print('\nМатрица:')
for i in range(4):
    for j in range(5):
        print(NewMas[i][j], end = " ")
    print()

for i in range(4):
    del NewMas[i][0]
    del NewMas[i][2]

print('\nМатрица после удаления 1 и 4 столбца:')
for i in range(4):
    for j in range(3):
        print(NewMas[i][j], end = " ")
    print()

NewMas2 = []
for i in range(3):
    NewMas2.append([0]*4)

for i in range(4):
    for j in range(3):
        NewMas2[j][i] = NewMas[i][j]

print('\nТранспонированная матрица после удаления:')
for i in range(3):
    for j in range(4):
        print(NewMas2[i][j], end = " ")
    print()
'''
import random
import numpy as np

n = 8

matrix = np.random.randint(-10, 11, size=(8, 8))
print(matrix)

center_part = matrix[2:6, 2:6]
print(center_part)

min_element = np.min(matrix)
print(min_element)

min_row = np.full((1, 8), min_element)
matrix = np.concatenate((min_row, matrix))
print(matrix)

sum_elements = np.sum(matrix)
mean_elements = np.mean(matrix)
print("Сумма элементов:", sum_elements)
print("Среднее арифметическое:", mean_elements)

'''
n = 8

mas = [0] * n
for i in range(n):
    mas[i] = [0] * n


print('Изначальная матрица:')
for i in range(n):
    for j in range(n):
        mas[i][j] = random.randint(-10, 10)
        print(mas[i][j], end = " ")
    print()

print('\nЦентральная часть матрицы:')
for i in range(2,n-2):
    for j in range(2,n-2):
        print(mas[i][j], end = " ")
    print()

minimum = 11
for i in range(0,n):
    if (min(mas[i]) < minimum):
        minimum = min(mas[i])

for i in range(n-1,-1,-1):
    if minimum in mas[i]:
        del mas[i]

print('\nМинимальное число:', minimum)
print('\nМатрица после удаления строк:')
for i in range(0,len(mas)):
    for j in range(0,n):
        print(mas[i][j], end = " ")
    print()


NewMas = []
for i in range(len(mas)+1):
    NewMas.append([0]*n)

print('\nМатрица после удаления строк и добавления строки из минимального элемента:')
for i in range(0,len(mas)+1):
    for j in range(0,n):
        if (i == 0):
            NewMas[i][j] = minimum
        else:
            NewMas[i][j] = mas[i-1][j]
        print(NewMas[i][j], end = " ")
    print()

summa = 0
for i in range(0,len(NewMas)):
    summa += sum(NewMas[i])
SrArif = summa / (len(NewMas) * n)
print('\nСумма всех элементов:', summa,'\nСреднее арифметическое:', SrArif)
'''
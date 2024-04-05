import random
import numpy as np

People = np.array(['Гена', 'Маша', 'Даша', 'Гена', 'Петя', 'Маша'])

'''
Score = []
for i in range(len(People)):
    Score.append([0]*(len(People)+2))
'''

Score = np.eye(len(People),len(People)+2)
print('\nУченики:', People)

print('\nОценки:')
for i in range(len(Score)):
    for j in range(len(People)+2):
        Score[i][j] = random.randint(1, 5)
        print(Score[i][j], end = " ")
    print()

PeopleName = input('\nВведите имя ученика: ')

mask = People == PeopleName

if np.any(mask):
    RowName = Score[mask]
    print(f'Оценки {PeopleName}: ', end= ' ')
    for row in RowName:
        print(row, end= ' ')


'''
for i in range(len(People)):
    if (People[i] == PeopleName):
        print(f'Оценки {PeopleName}: {Score[i]}')
'''
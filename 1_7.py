import fractions
import math

K = int(input('Введите количество дробей: '))
div = []
den = []

for i in range(0, K):
    div.append(int(input('\nВведите делитель: ')))
    den.append(int(input('Введите знаменатель: ')))

summa = 0
for i in range(0, K):
    summa += fractions.Fraction(div[i], den[i])

nod = 1
for i in range(0, K-1):
    nod = math.gcd(den[i], den[i+1])

print('Сумма дробей:', summa, '\nНОД:', nod)
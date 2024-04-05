s = input('Введите строку: ')

for i in range (0, len(s)):
    if i == 0: print('Первый символ:', s[i])
    elif i == (len(s)-1): print('Последний символ:', s[i])

print('Первый символ:', s[0])
print('Последний символ:', s[-1])
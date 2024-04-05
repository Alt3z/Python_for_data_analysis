s = input('Введите числа через пробел: ')
List = []

for i in s:
    if i not in List and i != ' ':
        List.append(i)

print('Количество неповторяющихся чисел:', len(List))
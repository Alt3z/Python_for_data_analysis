years_list = []
x = int(input('Введите год рождения: '))
years_list.append(x)

for i in range(years_list[0], years_list[0]+5):
    years_list.append(i+1)

print('3 день рождения был в:', years_list[3],'году')
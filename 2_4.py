years_list = []
x = int(input('Введите год рождения: '))
years_list.append(x)

for i in range(years_list[0], years_list[0]+5):
    years_list.append(i+1)

print('Список:', years_list)


years_list2 = [0,0,0,0,0,0]
years_list2[0] = x
years_list2[1] = x+1
years_list2[2] = x+2
years_list2[3] = x+3
years_list2[4] = x+4
years_list2[5] = x+5


print('Список:', years_list2)
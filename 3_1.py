
k = int(input('Введите количество стран: '))

country = []
all = {}

for i in range(0,k):
    print(i+1,' страна и города:')
    s = input()
    word = s.split(' ')
    j = 0
    sity = []
    for k in word:
        if j == 0:
            country.append(k)
            j += 1
        else:
            sity.append(k)

    all[country[i]] = sity

for i in range(3):
    s2 = input(f"Введите {i + 1} город для поиска: ")
    x = False

    for country, city in all.items():
        if s2 in city:
            print(f"Город {s2} расположен в стране {country}.")
            x = True

    if (x == False):
        print('Такого города нет')

import random

location = ['Спальня', 'Кухня', 'Ванная', 'Коридор', 'Окно', 'Дверь']
location2 = ['спальне', 'кухне', 'ванной', 'коридоре', 'окне', 'двери']
rand = random.randint(0, 3)
startlocation = location[rand]
startlocation2 = location2[rand]

while startlocation != 'Окно' and startlocation != 'Дверь':
    print('Вы в', startlocation2, '. Куда идем?')
    if startlocation == 'Спальня':
        NextStep = int(input('#1 - в ванную\n#2 - в коридор\n'))
        if NextStep != 1 and NextStep != 2:
            print('Данные не корректны')
        elif NextStep == 1:
            startlocation = 'Ванная'
            startlocation2 = 'ванной'
        elif NextStep == 2:
            startlocation = 'Коридор'
            startlocation2 = 'коридоре'
    elif startlocation == 'Кухня':
        NextStep = int(input('#1 - в коридор\n#2 - в окно\n'))
        if NextStep != 1 and NextStep != 2:
            print('Данные не корректны')
        elif NextStep == 1:
            startlocation = 'Коридор'
            startlocation2 = 'коридоре'
        elif NextStep == 2:
            startlocation = 'Окно'
            startlocation2 = 'окне'
            print('Вы выпали и разбились!')
    elif startlocation == 'Ванная':
        NextStep = int(input('#1 - в коридор\n#2 - в спальню\n'))
        if NextStep != 1 and NextStep != 2:
            print('Данные не корректны')
        elif NextStep == 1:
            startlocation = 'Коридор'
            startlocation2 = 'коридоре'
        elif NextStep == 2:
            startlocation = 'Спальня'
            startlocation2 = 'спальне'
    elif startlocation == 'Коридор':
        NextStep = int(input('#1 - в спальню\n#2 - в ванную\n#3 - на кухню\n#4 - в дверь\n'))
        if NextStep != 1 and NextStep != 2 and NextStep != 3 and NextStep != 4:
            print('Данные не корректны')
        elif NextStep == 1:
            startlocation = 'Спальня'
            startlocation2 ='спальне'
        elif NextStep == 2:
            startlocation = 'Ванная'
            startlocation2 ='ванной'
        elif NextStep == 3:
            startlocation = 'Кухня'
            startlocation2 ='кухне'
        elif NextStep == 4:
            startlocation = 'Дверь'
            startlocation2 ='двери'
            print('Вы выиграли!')
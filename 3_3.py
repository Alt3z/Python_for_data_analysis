import random

N = int(input('Введите максимальное число: '))
rand = int(input('Введите максимальное число, которое загадали: '))
print(rand)

check = []
MayBe = []
xx = False

while not xx:
    s = input('Введите числа через пробел или напишите "Помогите!", чтобы закончить: ')
    x = False
    checkNow = []
    if s != 'Помогите!':
        word = s.split(' ')
        if len(word) == 1:
            if int(word[0]) == rand:
                xx = True
        for d in word:
            check.append(int(d))
            checkNow.append(int(d))
        for j in checkNow:
            if j == rand:
                x = True
                break
        if x == True:
            print('Ответ Ивана: да')
            for k in check:
                MayBe.append(k)
        else:
            print('Ответ Ивана: нет')
    else:
        print('Возможные числа: ', end='')
        if len(MayBe) != 0:
            print(MayBe)
        else:
            for i in range(N//2):
                print(random.randint(0,N),end=' ')
            print()

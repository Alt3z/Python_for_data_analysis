s = input('Введите слово: ')

for i in range(0, len(s)//2):
    if s[i] != s[len(s)-i-1]:
        print('Ваше слово не палиндром!')
        break
else:
    print('Ваше слово палиндром!')

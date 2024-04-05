s = input("Введите упакованную строку: ")
NewS = ''
count = 1

for i in s:
    if i.isdigit():
        count = int(i)
    else:
        NewS += i * count
        count = 1

print("Исходная строка:", NewS)
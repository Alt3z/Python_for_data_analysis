summa = 0
x = True

while x:
    num = input("Введите число или 'stop' для завершения: ")
    if num == "stop":
        x = False
    else:
        summa += int(num)

print("Сумма введенных чисел:", summa)
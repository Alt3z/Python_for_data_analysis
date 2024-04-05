import random
import string

def password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input('Введите длину пароля: '))

print('Сгенерированный пароль:', password(length))
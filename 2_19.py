password = input('Введите пароль: ')
result = 'Пароль надежен'

special = '!@#$%^&*()-+'

if len(password) < 12:
    result = 'Пароль не надежен'
    print('Пароль должен содержать не менее 12 символов.')

if not any(char.isdigit() for char in password):
    result = 'Пароль не надежен'
    print('Пароль должен содержать хотя бы одну цифру.')

if not any(char.isupper() for char in password):
    result = 'Пароль не надежен'
    print('Пароль должен содержать хотя бы одну заглавную букву.')

if not any(char.islower() for char in password):
    result = 'Пароль не надежен'
    print('Пароль должен содержать хотя бы одну строчную букву.')

if not any(char in special for char in password):
    result = 'Пароль не надежен'
    print('Пароль должен содержать хотя бы один спецсимвол.')

print(result)
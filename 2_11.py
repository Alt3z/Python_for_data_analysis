import random

def multiplication (a,b):
    if a%2==0 and b%2==0:
        return a*b
    else:
        return -1


List = []
for i in range(0, 10):
    a = random.randint(0,50)
    b = random.randint(0, 50)
    List.append(multiplication(a,b))

print('Полученный список:', List)

import random

List = []
for i in range(0, 10):
    List.append(random.randint(0, 140))
print('Список1:', List)

List2 = []
for i in range(0, len(List)-1):
    if List[i+1] > List[i]:
        List2.append(List[i+1])
print('Список2:', List2)
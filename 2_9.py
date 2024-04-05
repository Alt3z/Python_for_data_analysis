import random

List1 = [random.randint(0, 140) for i in range(15)]
List2 = [List1[i] for i in range(len(List1)) if i % 2 == 0]

print(List2)
quantity = int(input("Введите количество человек: "))

genealogy_tree = {}

for i in range(quantity - 1):
    child, parent = input(f"{i + 1} пара: ").split()
    genealogy_tree[child] = parent

heights = {}


def calculate_height(person):
    if person not in heights:
        if person not in genealogy_tree:
            heights[person] = 0
        else:
            parent = genealogy_tree[person]
            heights[person] = calculate_height(parent) + 1
    return heights[person]


for person in genealogy_tree.keys():
    calculate_height(person)

for person in genealogy_tree.values():
    if person not in genealogy_tree:
        root = person

sorted_people = sorted(genealogy_tree.keys())
sorted_people.append(root)

sorted_people.sort()

for person in sorted_people:
    print(f"{person} {heights[person]}")
k = int(input("Введите кол-во заказов: "))
orders = {}
def sort_key(order):
    return order[0]

for i in range(k):
    order_data = input(f"{i + 1} заказ: ").split()
    buyer = order_data[0].strip()
    name = order_data[1].strip()
    count = int(order_data[2].strip())

    if buyer in orders:
        x = False
        for i, existing_name, existing_count in enumerate(orders[buyer]):
            if existing_name == name:
                orders[buyer][i] = (existing_name, existing_count + count)
                x = True
                break
        if x == False:
            orders[buyer].append((name, count))
    else:
        orders[buyer] = [(name, count)]

buyers = orders.keys()

for buyer in buyers:
    print(f"Покупатель {buyer}: ")
    total_order = 0
    sorted_orders = sorted(orders[buyer], key=sort_key)
    for pizza_name, count in sorted_orders:
        total_order += count
        print(f"Пицца {name}: {count}")

    print(f"Всего заказано пицц: {total_order}\n")
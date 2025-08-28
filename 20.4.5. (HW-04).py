import json
from collections import Counter

with open("orders_july_2023.json", "r") as my_file:
    orders = json.load(my_file)

max_price = 0
max_price_list = []
# цикл по заказам
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_price = price
for order_num, orders_data in orders.items():
    price = orders_data['price']
    if price == max_price:
        max_price_list.append(order_num)
print(f'1. Номер заказа(ов) с наибольшей стоимостью: {', '.join(max_price_list)}, \nстоимость заказа: {max_price}')

max_quantity = 0
max_quantity_list = []
for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        max_quantity = quantity
for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    if quantity == max_quantity:
        max_quantity_list.append(order_num)
print(f'\n2. Номер заказа(ов) с наибольшим количеством товаров: {', '.join(max_quantity_list)}, \nколичество товаров: {max_quantity}')

# В какой день в июле было сделано больше всего заказов?
count_orders={}
for order_num, orders_data in orders.items():
    date = orders_data['date']
    if date in count_orders:
        count_orders[date] += 1
    else:
        count_orders[date] = 1
max_count = max(count_orders, key=count_orders.get)
max_value = count_orders[max_count]
list_max_count = []
for date in count_orders:
    if count_orders.get(date) == max_value:
        list_max_count.append(date[5:7])
print(f"\n3. В июле больше всего заказов было сделано {', '.join(list_max_count)} числа, \nколичество заказов: {count_orders[max_count]}")

# Какой пользователь сделал самое большое количество заказов за июль?
count_u_orders={}
for order_num, orders_data in orders.items():
    user = orders_data['user_id']
    if user in count_u_orders:
        count_u_orders[user] += 1
    else:
        count_u_orders[user] = 1
max_u_count=max(count_u_orders, key=count_u_orders.get)
max_u_value=count_u_orders[max_u_count]
list_max_u_count = []
for user in count_u_orders:
    if count_u_orders.get(user) == max_u_value:
        list_max_u_count.append(user)
print(f"\n4. В июле больше всего заказов было сделано пользователем(ями) с ID {', '.join([str(i) for i in list_max_u_count])}, \nколичество заказов {max_u_value}")

# У какого пользователя самая большая суммарная стоимость заказов за июль?
total_cost= {}
cost = 0
for order_num, orders_data in orders.items():
    user = orders_data['user_id']
    cost = orders_data['price']
    if user not in total_cost:
        total_cost[user] = cost
    else:
        total_cost[user] += cost
max_total_cost=max(total_cost, key=total_cost.get)
max_total_value=total_cost[max_total_cost]
list_total_cost = []
for user in total_cost:
    if total_cost.get(user) == max_total_value:
        list_total_cost.append(user)
print(f'\n5. В июле y пользователя(ей) с ID {', '.join([str(i) for i in list_total_cost])}, \nнаибольшая суммарная стоимость заказов {max_total_value}')

# Какая средняя стоимость заказа была в июле?
# Какая средняя стоимость товаров в июле?
total_price=0
total_quantity=0
for order_num, orders_data in orders.items():
    price = orders_data['price']
    quantity = orders_data['quantity']
    total_price += price
    total_quantity += quantity
print(f'\n6. Средняя стоимость товаров в июле {'{:.2f}'.format(total_price/len(orders))}')
print(f'\n7. Средняя стоимость товаров в июле {'{:.2f}'.format(total_price/total_quantity)}')

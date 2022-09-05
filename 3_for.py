"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""


def sale_counter():
    sold_phones_data = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

    position1 = sold_phones_data[0].get('items_sold')
    sum1 = sum(position1)
    average1 = sum1 // len(position1)

    position2 = sold_phones_data[1].get('items_sold')
    sum2 = sum(position2)
    average2 = sum2 // len(position2)

    position3 = sold_phones_data[2].get('items_sold')
    sum3 = sum(position3)
    average3 = sum3 // len(position3)

    total_sum = sum1 + sum2 + sum3
    total_average = total_sum // len(position1) + len(position2) + len(position3)

    return f'Суммарное количество продаж iPhone 12: {sum1}, в среднем: {average1}\n\
Суммарное количество продаж Xiaomi Mi11: {sum2}, в среднем: {average2}\n\
Суммарное количество продаж Samsung Galaxy 21: {sum3}, в среднем: {average3}\n\
Всего продано: {total_sum} телефонов, в среднем продавалось: {total_average}'


print(sale_counter())

if __name__ == "__main__":
    sale_counter()


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


stock = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
    
def main(sales):
    sales_all = 0
    sales_avg_all = 0
    for i in range(len(stock)):
        sales_phone = 0
        for j in range(len(stock[i]['items_sold'])):
            sales_phone += stock[i]['items_sold'][j]
            sales_all += stock[i]['items_sold'][j]
            sales_avg = sales_all // len((stock[i]['items_sold']))
        sales_avg_all += sales_avg
        print(f'Сумма продаж {sales[i]["product"]} - {sales_phone}')
        print(f'Средняя сумма продаж {sales[i]["product"]} - {sales_avg}')
    print(f'Сумма продаж всех товаров - {sales_all}')
    print(f'Средняя сумма продаж всех товаров - {sales_avg_all}')

if __name__ == "__main__":
    main(stock)
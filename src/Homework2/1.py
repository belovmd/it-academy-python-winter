"""
1. Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество L товара
Посчитайте общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
"""

n = input().split()
basket = []
for i in n:
    if i.isdigit():
        basket.append(int(i))
cost_kopeek = (basket[0] * 100 + basket[1]) * basket[2]
print('Общая цена', cost_kopeek // 100, 'рублей', cost_kopeek % 100, 'копеек.')

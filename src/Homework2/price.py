"""1. Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена,
а также количество L товара Посчитайте общую цену в
 рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек"""
# Порядок ввода числовых данных в строке - рубли, копейки, кол-во.
# Разделитель какой угодно, числа целые, положительные.
data = (input("Ведите данные: "))
i = 0
temp = rubles = coins = quantity = ''
# Находим численные значения в строке
while i < len(data):
    if '0' <= data[i] <= '9':
        while i < len(data):
            if '0' <= data[i] <= '9':
                temp += data[i]
                i += 1
            else:
                i += 1
                break
        if rubles == '' and temp != '':
            rubles = temp
        elif coins == '' and temp != '':
            coins = temp
        elif quantity == '' and temp != '':
            quantity = temp
        else:
            break
        temp = ''
    else:
        i += 1
print('Общая цена %d рублей %d копеек' %
      ((int(rubles) + (int(coins) // 100)) * int(quantity),
       (int(coins) % 100) * int(quantity)))

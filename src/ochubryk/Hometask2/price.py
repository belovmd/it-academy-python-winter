# Напишите программу, которая считает общую цену.
# Вводится M рублей и N копеек цена, а также количество L товара
# Посчитайте общую цену в рублях и копейках за L товаров.
rubles = int(input('Введите рубли: '))
pennies = int(input('Введите копейки: '))
count = int(input('Введите количество товара: '))

total_pennies = (pennies * count) + (rubles * 100 * count)
total_rubles = total_pennies // 100
remaining_pennies = total_pennies % 100

n, p = remaining_pennies % 100, total_rubles % 100
n1, p1 = n % 10, p % 10
if 10 < n < 20:
    word_pennies = 'копеек'
elif 1 < n1 < 5:
    word_pennies = 'копейки'
elif n1 == 1:
    word_pennies = 'копейка'
else:
    word_pennies = 'копеек'

if 10 < p < 20:
    word_rubles = 'рублей'
elif 1 < p1 < 5:
    word_rubles = 'рубля'
elif p1 == 1:
    word_rubles = 'рубль'
else:
    word_rubles = 'рублей'

print('Общая цена: ', total_rubles, word_rubles,
      remaining_pennies, word_pennies)

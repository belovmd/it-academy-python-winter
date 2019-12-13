# Напишите программу, которая считает общую цену.
M_rubles, N_pennies = int(input('Введите рубли: ')), int(input('Введите копейки: '))
L_count = int(input('Введите количество товара: '))

All_N_pennies = N_pennies * L_count
if All_N_pennies > 99:
    Rubles_from_pennies = All_N_pennies // 100
    Remaining_pennies = All_N_pennies % 100
    Result_rubles = (M_rubles * L_count) + Rubles_from_pennies
else:
    Remaining_pennies = All_N_pennies
    Result_rubles = M_rubles * L_count

n, p = Remaining_pennies % 100, Result_rubles % 100
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

print('Общая цена: ', Result_rubles, word_rubles, Remaining_pennies, word_pennies)

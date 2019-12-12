"""
1. Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество L товара.
Посчитайте общую цену в рублях и копейках за L товаров.
"""

pr_rub = int(input('Введитецену в рублях\n'))
pr_kop = int(input('Введите копейки (меньше ста)\n'))
if pr_rub >= 0 and 0 <= pr_kop < 100:
    print('Цена', pr_rub, 'руб', pr_kop, 'коп')
    item_count = int(input('Введите количество товара\n'))
    (full_pr_rub, full_pr_kop) = (pr_rub * item_count, pr_kop * item_count)
    if full_pr_kop >= 100:
        full_pr_rub += full_pr_kop // 100
        full_pr_kop %= 100
    print('Итого', item_count, 'шт', full_pr_rub, 'руб', full_pr_kop, 'коп')
else:
    print('Введите верные числа\n')

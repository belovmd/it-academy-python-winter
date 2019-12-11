price_rub = int(input('Введитецену в рублях\n'))
price_kop = int(input('Введите копейки (меньше ста)\n'))
if price_rub >= 0 and 0 <= price_kop < 100:
    print('Цена', price_rub, 'руб', price_kop, 'коп')
    item_count = int(input('Введите количество товара\n'))
    (full_price_rub, full_price_kop) = (price_rub * item_count, price_kop * item_count)
    if full_price_kop >= 100:
        full_price_rub += full_price_kop // 100
        full_price_kop %= 100
    print('Итоговая цена за', item_count, 'шт равна', full_price_rub, 'руб', full_price_kop, 'коп')
else:
    print('Введите верные числа\n')

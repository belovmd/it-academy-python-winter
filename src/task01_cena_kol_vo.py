m = int(input('введите стоимость рублей:'))
n = int(input('введите стоимость копеек:'))
l = int(input('введите к-во товара:'))
print('Общая цена:', (m * l + (n * l // 100)), 'рублей', n * l % 100, 'копеек')


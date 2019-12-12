# Посчитать стоимость
m = int(input('Введите стоимость вещи (руб):'))
n = int(input('Введите стоимость вещи (коп):'))
l = int(input('Введите колличество товара, которое хотите купить:'))
# Узнаем, сколько руб и коп стоит вещь
cost1 = m * l
cost2 = n * l
# Если копеек больше 100, остаток переведем в рубли
while cost2 >= 100:
    cost3 = cost2 // 100
    cost1 = cost1 + cost3
    cost2 = cost2 - (cost3 * 100)
# Сделаем красивый вывод ответа,
# что бы не было ( "стоит 22 рублей" или "стоит 1 копеек")
# Для этого узнаем, на какую цифру заканчивается число рублей и копеек
# для рублей:
s = str(cost1)
costrub = int(s[-1])
# для копеек используем другой способ, без приведения к строке, но интереснее:
costcop1, costcop2 = cost2 / 10, cost2 // 10
costcop = int((costcop1 - costcop2) * 10)
# делаем красивый output:
# сначала рубли
if costrub == 0 or costrub == 5 or costrub == 6 or cost1 == 11:
    print('Общая цена: {0} рублей'.format(cost1), end="")
# создаю такой же output для 7, 8 и 9
# потому что если их засунуть в if, будет слишком длинная строка
elif costrub == 7 or costrub == 8 or costrub == 9:
    print('Общая цена: {0} рублей'.format(cost1), end="")
elif costrub == 2 or costrub == 3 or costrub == 4:
    print('Общая цена: {0} рубля'.format(cost1), end="")
elif costrub == 1:
    print('Общая цена: {0} рубль'.format(cost1), end="")
# теперь копейки
if costcop == 2 or costcop == 3 or costcop == 4:
    print(' {0} копейки'.format(cost2))
elif costcop == 5 or costcop == 6 or cost2 == 11:
    print(' {0} копеек'.format(cost2))
elif costcop == 7 or costcop == 8 or costcop == 9:
    print(' {0} копеек'.format(cost2))
elif costcop == 1:
    print(' {0} копейку'.format(cost2))
# получилось объемно, зато красиво )

# Посчитать стоимость
rub_input = int(input('Введите стоимость вещи (руб):'))
cop_input = int(input('Введите стоимость вещи (коп):'))
quant = int(input('Введите колличество товара, которое хотите купить:'))
cost1 = rub_input * quant
cost2 = cop_input * quant
# Если копеек больше 100, остаток переведем в рубли
while cost2 >= 100:
    cost3 = cost2 // 100
    cost1 = cost1 + cost3
    cost2 = cost2 - (cost3 * 100)
s = str(cost1)
cost_rub = int(s[-1])
# для копеек используем другой способ, без приведения к строке, но интереснее:
cost_cop1, cost_cop2 = cost2 / 10, cost2 // 10
cost_cop = int((cost_cop1 - cost_cop2) * 10)
# делаем красивый output:
if cost_rub == 0 or cost_rub == 5 or cost_rub == 6 or cost1 == 11:
    print('Общая цена: {0} рублей'.format(cost1), end="")
# создаю такой же output для 7, 8 и 9
# потому что если их засунуть в if, будет слишком длинная строка
elif cost_rub == 7 or cost_rub == 8 or cost_rub == 9:
    print('Общая цена: {0} рублей'.format(cost1), end="")
elif cost_rub == 2 or cost_rub == 3 or cost_rub == 4:
    print('Общая цена: {0} рубля'.format(cost1), end="")
elif cost_rub == 1:
    print('Общая цена: {0} рубль'.format(cost1), end="")
# теперь копейки
if cost_cop == 2 or cost_cop == 3 or cost_cop == 4:
    print(' {0} копейки'.format(cost2))
elif cost_cop == 5 or cost_cop == 0 or cost_cop == 6 or cost2 == 11:
    print(' {0} копеек'.format(cost2))
elif cost_cop == 7 or cost_cop == 8 or cost_cop == 9:
    print(' {0} копеек'.format(cost2))
elif cost_cop == 1:
    print(' {0} копейку'.format(cost2))

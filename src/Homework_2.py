# денежный калькулятор
paper = int(input('сколько рублей: \n'))
coins = int(input('сколько копеек: \n'))
howMany = (int(input('количество товара: \n')))
cost = howMany * ((paper * 100) + coins)
rub = cost // 100
kop = cost % 100
print('товар стоит ', rub, 'руб.', kop, 'коп.')

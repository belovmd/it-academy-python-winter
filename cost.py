m = int(input("Введите кол-во рублей\n"))
n = int(input("Введите кол-во копеек\n"))
numGoods = int(input("Введите кол-во покупаемого товара\n"))
costn = n * numGoods / 100
cost = costn + (m * numGoods)
print("Общая цена составляет", cost, "рублей")
print("Или", cost // 1, "руб.", round((cost - (cost // 1)) * 100), "коп.")

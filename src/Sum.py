"""
Напишите программу, которая считает общую цену. Вводится M рублей и N копеек
цена, а также количество L товара Посчитайте общую цену в рублях и копейках
за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
Напишите программу, которая считает общую цену. Вводится M рублей и N копеек
цена, а также количество L товара Посчитайте общую цену в рублях и копейках за
L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
"""

rub = int(input("Введите количество рублей: "))  # rubles
kop = int(input("Введите количество копеек: "))  # pennies
if len(str(kop)) >= 3:  # if len pennies > 2 symbols
    newrub = (rub * 100 + kop) // 100
    newkop = kop % 100
    price = newrub + newkop / 100
else:
    newrub = rub
    newkop = kop
    price = newrub + newkop / 100
# quntaty of purchase
qun = int(input("Введите количество, чтобы расчитать сумму покупки: "))
sumrub = int(price * qun // 1)  # summ in rubles
endrub = (sumrub - (sumrub // 1000) * 1000)
# identify rubles word endding
end1 = ""
if endrub % 10 == 0:
    end1 = str("ей")
elif endrub % 100 in range(5, 10):
    end1 = str("ей")
elif endrub % 100 in range(9, 20):
    end1 = str("ей")
elif endrub % 10 == 1:
    end1 = str("ь")
elif endrub % 10 in range(1, 5):
    end1 = str("я")
# identify pennies word endding
end2 = ""
if kop % 10 == 0:
    end2 = str("ек")
elif kop % 10 in range(5, 10):
    end2 = str("ек")
elif kop % 100 in range(9, 20):
    end2 = str("ек")
elif kop % 10 == 1:
    end2 = str("йка")
elif kop % 10 in range(1, 5):
    end2 = str("йки")
sumkop = int(round((price * qun % 1), 2) * 100)  # sum pennies
print("Сумма покупки:", sumrub, "рубл" + end1, end=" ")
print(sumkop, "копе" + end2)

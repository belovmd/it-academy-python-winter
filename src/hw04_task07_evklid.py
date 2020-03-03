"""
Даны два натуральных числа.
Вычислите их наибольший общий делитель
при помощи алгоритма Евклида
(мы не знаем функции и рекурсию).
----------------------------------
"""

number01 = int(input('число1:'))
number02 = int(input('число2:'))
while number02 != 0:
    number01, number02 = number02, number01 % number02
print(number01)

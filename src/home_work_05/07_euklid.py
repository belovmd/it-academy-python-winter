"""
Даны два натуральных числа.
Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
"""

first_num = int(input('Введите первое число\n'))
second_num = int(input('Введите второе число\n'))
while first_num and second_num:
    if first_num > second_num:
        first_num %= second_num
    else:
        second_num %= first_num
print(first_num + second_num)

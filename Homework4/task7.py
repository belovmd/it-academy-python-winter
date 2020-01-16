# 7. Оглянемся назад.
# Даны два натуральных числа.
# Вычислите их наибольший общий делитель при помощи алгоритма Евклида
# (мы не знаем функции и рекурсию).

number1 = int(input('Enter 1st natural number: '))
number2 = int(input('Enter 2nd natural number: '))
while number1 != number2:
    if number1 > number2:
        number1 = number1 - number2
    else:
        number2 = number2 - number1

print("GCD =", number1)  # greatest common divisor

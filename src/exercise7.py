# Даны два натуральных числа. Вычислите их наибольший
# общий делитель при помощи алгоритма Евклида
# (мы не знаем функции и рекурсию).

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

while a != b and a != 0 and b != 0:
    if a > b:
        a = a - b
    else:
        a, b = b, a
        a = a - b
print(a)

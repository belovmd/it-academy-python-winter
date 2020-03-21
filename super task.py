# Даны два натуральных числа.
# Вычислите их наибольший общий
# делитель при помощи алгоритма
# Евклида (мы не знаем функции и рекурсию)

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
while first_number != second_number:
    if first_number > second_number:
        first_number = first_number - second_number
    else:
        second_number = second_number - first_number
print(first_number)

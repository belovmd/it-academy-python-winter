"""- Определите, является ли число палиндромом
(читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами (без конвертации числа в строку)"""
t_number = number = abs(int(input("Введите целое положительное число: ")))
digit = len(str(number)) - 1
re_number = re_digit = 0
# ( n00000 => 00000m )
while re_digit <= len(str(number)) - 1:
    re_number += (t_number // (10 ** digit)) * (10 ** re_digit)
    t_number = t_number % (10 ** digit)
    re_digit += 1
    digit -= 1
if number == re_number:
    print("Введенное число палиндром")
else:
    print("Введенное число не палиндром")

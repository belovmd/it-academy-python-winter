# - Определите, является ли число палиндромом
# (читается слева направо и справа налево одинаково).
# Число положительное целое, произвольной длины.
# Задача требует работать только с числами (без конвертации числа в строку)

num = int(input("Checking the number on the palindrome: ", ))
rev = 0
double_num = num
while double_num > 0:
    rev = 10 * rev + double_num % 10
    double_num //= 10
if rev == num:
    print('palindrome')

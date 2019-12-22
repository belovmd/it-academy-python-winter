# Определите, является ли число палиндромом (читается слева направо и справа
# налево одинаково).  Число положительное целое, произвольной длины. Задача
# требует работать только с числами (без конвертации числа в строку)

number = int(input('Введите число: '))
user_number = number
rev_number = 0
while number:
    low = number % 10
    number //= 10
    rev_number = rev_number * 10 + low
print(rev_number)

if rev_number == user_number:
    print('Число палиндром! ')
else:
    print('Число не палиндром! ')

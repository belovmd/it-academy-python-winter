"""
Определите, является ли число палиндромом
(читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами
(без конвертации числа в строку)
"""

num = int(input('Введите число\n'))
num_length = 1
num_division = num
while num_division // 10 > 0:
    num_length += 1
    num_division //= 10
print('Длина числа', num_length)

num_length_2 = num_length  # для второго варианта

# Вариант 1
num_x = num
for i in range(num_length // 2):
    n1 = num_x // 10 ** (num_length - 1)
    n2 = num_x % 10
    print('Сравниваем крайние цифры', n1, n2)
    num_x = (num_x - n1 * 10 ** (num_length - 1)) // 10
    num_length -= 2
    if n1 != n2:
        print(num, 'не палиндром')
        break
else:
    print(num, 'палиндром')

# Вариант 2 (revert number using arithmetic operators)
new_num = 0
cur_num = num
for x in range(num_length_2):
    n_end = cur_num % 10
    cur_num = (cur_num - n_end) // 10
    new_num = new_num * 10 + n_end
if num == new_num:
    print(num, 'палиндром')
else:
    print(num, 'не палиндром')

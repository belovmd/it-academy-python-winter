# Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы. n - вводится

number = int(input('сколько первых чисел Фибоначчи вы хотите увидеть: '))

first = 0
second = 1

for i in range(number):
    print(first)
    first, second = second, first + second

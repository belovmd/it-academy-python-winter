# Числа Фибоначи
# Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы. n - вводится
num = int(input('Введите число '))
num_1 = 0
num_2 = 0
for i in range(num + 1):
    if i == 0 or i == 1:
        num_1 = i
        num_2 = num_2 + num_1
        print(1, end=' ')
    else:
        num_1, num_2 = num_2, num_1 + num_2
        print(num_2, end=' ')

n = int(input('Введите число\n'))

(n_1, n_2) = (0, 1)
print('Вариант 1')
print(n_1, n_2, end=' ')
for i in range(2, n):
    n_x = n_1  # временные переменные для хранения прошлых значений по заданию
    n_1 = n_2
    n_2 = n_x + n_2
    print(n_2, end=' ')

(num_1, num_2) = (0, 1)
print('\nВариант 2')
print(num_1, num_2, end=' ')
for i in range(2, n):
    (num_1, num_2) = (num_2, num_1 + num_2)  # более простой вариант
    print(num_2, end=' ')

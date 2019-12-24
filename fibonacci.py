'''Выведите n-ое число Фибоначчи, используя только временные переменные, циклические операторы и условные операторы.
n - вводится '''

n = int(input('Введите число: '))
fib1 = fib2 = 1

if n < 2:
    print(n)
else:
    print(fib1, end=' ')
    print(fib2, end=' ')
    for i in range(2, n):
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
        print(fib3, end=' ')

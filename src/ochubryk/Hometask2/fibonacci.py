n = int(input('Введите порядковый номер числа Фибоначчи: '))
fib1 = fib2 = 1

if n < 2:
    print('Первый элемент ряда Фибоначчи: 1')
else:
    print('Числа ряда Фибоначчи до искомого элемента(включительно): ')
    print(fib1, end=' ')
    print(fib2, end=' ')

    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2

        print(fib2, end=' ')

    print('\nЧисло Фибоначчи ' + str(n) + ' ' + ' это: ' + str(fib2))

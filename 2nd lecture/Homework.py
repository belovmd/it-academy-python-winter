# Вывести кубы первых n чисел, где n вводит пользователь.

n = int(input('Введите целое число: ', ))
for i in range(1, n + 1):
    print(i ** 3, '')

# Проверьте, является ли введенное число простым.

if n > 1:
    s = 0
    for i in range(1, n + 1):
        if n % i == 0:
            s += 1
    if s == 2:
        print('простое')
    else:
        print('составное')

# ***Проверьте, является ли число палиндромом

s = 0
m = n
while m > 0:
    s = 10 * s + m % 10
    m //= 10
if s == n:
    print('палиндром')

n = str(n)
if n == n[::-1]:
    print('палиндром')

# ***Выведите первые n чисел Фибоначчи,
# используйте временные переменные для хранения прошлых значений и цикл for

n = int(n)
f = 0
f0 = 0
f1 = 1
if n == 1:
    print(0)
elif n == 2:
    print(0)
    print(1)
else:
    print(0)
    print(1)
    for i in range(1, n - 1):
        f = f1 + f0
        f0 = f1
        f1 = f
        print(f)

"""
task_1: Проверьте, является ли введенное число простым.
"""
var = int(input("Введите число. var="))
if var < 2:
    print("Необходимо ввести число 2 или больше")
else:
    i = 2
    while i <= var**0.5:
        if var % i == 0:
            print(var, "-составное число")
            break
        i += 1
    else:
        print(var, "-простое число")

"""
task_2: Вывести кубы первых n чисел, где n вводит пользователь.
"""
var = int(input("Введите количество n первых чисел для подсчета кубов, var="))
for i in range(var):
    p = i + 1
    print(p, '**3=', p ** 3)

"""
task_3: Определите, является ли число палиндромом (читается слева направо
и справа налево одинаково). Число положительное целое, произвольной длины.
Задача требует работать только с числами (без конвертации числа в строку)
"""
numb = int(input("Введите натуральное число numb="))
int_val = numb
mod_numb = 0
while int_val:
    mod_numb = mod_numb * 10 + int_val % 10
    int_val //= 10
if mod_numb == numb:
    print(numb, "является палиндромом")
else:
    print(numb, "не является палиндромом")

""""
task_4: Выведите n-ое число Фибоначчи, используя только временные
переменные, циклические операторы и условные операторы. n - вводится
"""
fib_count = int(input("Введите количество первых чисел из ряда Фибоначчи. n="))
fib1 = fib2 = 1
fib12 = 0
if fib_count == 1:
    print(fib1)
elif fib_count == 2:
    print(fib1)
    print(fib2)
else:
    print(fib1)
    print(fib2)
    for i in range(fib_count - 2):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2)

# 1. Оформите решение задач из прошлых домашних работ в функции.


# 1. Создайте словарь с помощью генератора словарей так,
# чтобы его ключами были числа от 1 до 20, а значениями - кубы этих чисел.

def dct():
    dct_ = {number: number ** 3 for number in range(1, 14)}
    print(dct_)
    return dct_


# 2. Напишите программу, которая печатает цифры от 1 до 100,
# но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
# а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz.

def fizzbuzz():
    lst = []
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            lst.append('FizzBuzz')
        elif num % 3 == 0:
            lst.append('Fizz')
        elif num % 5 == 0:
            lst.append('Buzz')
        else:
            lst.append(str(num))

    # Вывод результата по 25 элементов в строке чтобы поместить на экран.
    for num_string in range(1, 5):
        print(' '.join([lst[num]
                        for num in range((num_string - 1) * 25,
                                         num_string * 25)]))


# 3. Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.

def list_to_tuple():
    lst1 = ['a', 'b', 'c']
    tpl1 = tuple(lst1)
    print(tpl1)
    return tpl1


# 4. Даны два натуральных числа.
# Вычислите их наибольший общий делитель при помощи алгоритма Евклида

def gcd():
    number1 = int(input('Enter 1st natural number: '))
    number2 = int(input('Enter 2nd natural number: '))
    data = str(number1) + ' ' + str(number2)   # Для записи в файл
    while number1 != number2:
        if number1 > number2:
            number1 = number1 - number2
        else:
            number2 = number2 - number1
    print('GCD =', number1)  # greatest common divisor
    data = data + ' GCD = ' + str(number1)
    return data


# Для проверки task1(runner).py:
# def check(a):
#     m = 5 * 5
#
# i = 0


# Variant №1

# def runner(*functions):
#     if not functions:
#         dct()
#         print()
#         fizzbuzz()
#         print()
#         list_to_tuple()
#         print()
#     else:
#         for func in functions:
#             func()
#             print()

# runner()
# runner(fizzbuzz)
# runner(list_to_tuple, dct)

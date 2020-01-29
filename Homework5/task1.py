# 1. Оформите решение задач из прошлых домашних работ в функции.


def dct():
    dct_ = {number: number ** 3 for number in range(1, 14)}
    print(dct_)


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


def list_to_tuple():
    lst1 = ['a', 'b', 'c']
    tpl1 = tuple(lst1)
    print(tpl1)


def runner(*functions):
    if not functions:
        dct()
        print()
        fizzbuzz()
        print()
        list_to_tuple()
        print()
    else:
        for func in functions:
            func()
            print()

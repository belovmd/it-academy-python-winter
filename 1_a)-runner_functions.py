"""Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
runner() – все фукнции вызываются по очереди"""

import copy


def function1():
    for numeric in range(101):
        if numeric % 3 == 0 and numeric % 5 == 0:
            print('FizzBuzz')
        elif numeric % 5 == 0:
            print('Buzz')
        elif numeric % 3 == 0:
            print('Fizz')
        else:
            print(numeric)


def function2():
    lst1 = [a + b for a in "ab" for b in ['b', 'c', 'd']]
    print(lst1)  # ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
    lst2 = lst1[::2]
    print(lst2)  # ['ab', 'ad', 'bc']
    lst3 = [a + b for a in '1234' for b in ['a']]
    print(lst3)  # ['1a', '2a', '3a', '4a']

    del lst3[1]
    print(lst3)  # ['1a', '3a', '4a']
    lst4 = copy.copy(lst3)
    print(lst4)  # ['1a', '3a', '4a']
    lst4.insert(1, '2a')
    print(lst4)  # ['1a', '2a', '3a', '4a']


def function3():
    tpl1 = tuple(['a', 'b', 'c'])
    print(tpl1)  # ('a', 'b', 'c')
    lst1 = list(tpl1)
    print(lst1)  # ['a', 'b', 'c']
    a, b, c = 'n', 2, 'python'
    print(a, b, c)  # n 2 python
    tpl2 = (123,)
    print(len(tpl2))  # 1
    for i in str(tpl2)[1:4]:
        # хотим получить отдельно три элемената
        #  из одного элемента кортежа
        print(i, end=',')  # 1,2,3,


def runner():
    function1()
    print('\nследующая функция')
    function2()
    print('\nследующая функция')
    function3()
    print('\nэта функция была последенй')


runner()

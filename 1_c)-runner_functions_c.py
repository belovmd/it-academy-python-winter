import copy

"""Оформите решение задач из прошлых домашних работ в функции. 
Напишите функцию runner.
runner(‘func’, ‘func1’...) - вызывает все переданные функции """


def function1():

    """1.FizzBuzz
    Напишите программу, которая печатает цифры от 1 до 100,
    о вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный
    5 пишет Buzz,
     а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
    """

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

    """ 2. List practice
    Используйте генератор списков чтобы получить следующий:
     ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
    Используйте на предыдущий список slice чтобы получить
    следующий: ['ab', 'ad', 'bc'].
    Используйте генератор списков чтобы получить следующий
    ['1a', '2a', '3a', '4a'].
    Одной строкой удалите элемент  '2a' из прошлого списка
    и напечатайте его.
    Скопируйте список и добавьте в него элемент '2a' так
    чтобы в исходном списке этого элемента не было.
    """

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

    """ 3 Tuple practice
    Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
    Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
    Сделайте следующие присвоения одной строкой a = 'a',
    b=2, c=’python’.
    Создайте кортеж из одного элемента, чтобы при
    итерировании по этому
    элементы последовательно выводились значения
    1, 2, 3. Убедитесь что len()
    исходного кортежа возвращает 1.
    """
    
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


def runner(*args):
    functions = {'function1': function1, 'function2': function2, 'function3': function3}
    for arg in args:
        functions[arg]()


runner('function3', 'function2')

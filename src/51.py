"""Оформите решение задач из прошлых домашних
 работ в функции. Напишите функцию runner."""
"""1 runner() – все фукнции вызываются по очереди"""


def func1():
    for num in range(1, 101):
        if num % 15 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("buzz")
        elif num % 5 == 0:
            print("fizz")
        else:
            print(num)


def func2():
    lst1 = [first + second for first
            in "ab" for second in "bcd"]
    print(lst1)
    print(lst1[::2])
    lst2 = [first + second for first
            in "1234" for second in "a"]
    print(lst2)
    print(lst2.pop(1))
    lst3 = lst2.copy()
    lst3.append('2a')
    print(lst2, lst3)


def func3():
    lst = ['a', 'b', 'c']
    tup_lst = tuple(lst)
    print(tup_lst, type(tup_lst))
    tup = ('a', 'b', 'c')
    lst_tup = list(tup)
    print(lst_tup, type(lst_tup))
    a, b, c = 'a', '2', 'python'
    print(a, b, c)
    tupl = ([1, 2, 3],)
    print(len(tupl), tupl)
    for element in tupl[0]:
        print(element)


def runner():
    print("first function: ")
    func1()
    print("second function: ")
    func2()
    print("last function: ")
    func3()


runner()

"""2 runner(‘func_name’) – вызывается только функцию func_name."""


def runner(func):
    function = {1: func1, 2: func2, 3: func3}
    function[func]()


num = int(input("Enter number of function: "))
runner(num)

"""3 runner(‘func’, ‘func1’...) - вызывает все переданные функции """


def runner(*args):
    function = {'func1': func1, 'func2': func2, 'func3': func3}
    for arg in args:
        function[arg]()


runner('func2', 'func3')

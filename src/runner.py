"""
Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""
import string


def func_1():
    null_str = ''
    input_line = 'abc cde def'

    for p in input_line.split():
        f = p.strip(string.punctuation)
        for el in f:
            if el not in null_str:
                null_str += el

    print(null_str)


def func_2():
    lst_gen = [a + b for a in 'abbcc' for b in ['a', 'b', 'c']]
    for el in lst_gen:
        if lst_gen.count(el) == 1:
            print(el)


def func_3():
    lst_ = [1, 2, 0, 5, 0, 7, 8, 9, 0]
    print([el for el in lst_ if el] + [0] * lst_.count(0))


def runner(*args):
    functions = {'func_1': func_1,
                 'func_2': func_2,
                 'func_3': func_3
                 }
    if not args:
        args = functions.keys()
    for arg in args:
        print(arg)
        functions[arg]()


runner()
runner('func_2')
runner('func_3', 'func_1')

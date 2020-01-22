"""
Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

import all_func


def runner(*args):
    if args is ():
        func_list = [el for el in dir(all_func) if not el.startswith('__')]
    else:
        func_list = [*args]

    for func in func_list:
        try:
            func = getattr(all_func, func)
            print(func())
        except AttributeError:
            print('No such func', func)
    return


runner()
runner('euklid')
runner('pair_elem')
runner('languages', 'diff_words')

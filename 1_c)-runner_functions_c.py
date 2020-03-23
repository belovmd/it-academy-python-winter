"""
Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

import myfunctions
import inspect


def runner(*args):
    if not args:
        func_list = [el for el in dir(myfunctions) if not el.startswith('__')]
    else:
        func_list = [*args]
    for func in func_list:
        try:
            func = getattr(myfunctions, func)
            print(func())
            if inspect.isfunction(func):
                print('Running function:', func.__name__)
                print('Result', func())
        except AttributeError:
            print('No such func', func)
    return

runner('function3')
runner('function2')
runner('function1', 'function0')
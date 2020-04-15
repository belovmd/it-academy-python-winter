# Оформите решение задач из прошлых домашних работ в функции.
# Напишите функцию runner.
# runner() – все фукнции вызываются по очереди
# runner(‘func_name’) – вызывается только функцию func_name
# runner(‘func’, ‘func1’...) - вызывает все переданные функции

import inspect
import my_func


def runner(*args):
    if not args:
        func_list = [el for el in dir(my_func) if not el.startswith('__')]
    else:
        func_list = [*args]

    for func in func_list:
        try:
            func = getattr(my_func, func)
            if inspect.isfunction(func):
                print('Функция:', func.__name__)
                print('Результат:', func())
        except AttributeError:
            print('Такой функции не существует', func)
    return


runner()
runner('euklid')
runner('pair_elem')
runner('languages', 'diff_words')

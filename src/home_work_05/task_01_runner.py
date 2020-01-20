"""
Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

import all_func


def runner(*args):
    func_list = ['all_func.' + elem for elem in dir(all_func) if '__' not in elem]
    print(func_list)
    for func in func_list:
        print(func)
    return


runner()

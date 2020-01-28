"""Оформите решение задач из прошлых домашних
 работ в функции. Напишите функцию runner.
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""
import my_functions


def runner(*functions):
    if not functions:
        for i in dir(my_functions):
            if '__' in i or 're' in i:
                pass
            else:
                functions = list(functions)
                functions.append(i)
    for function in functions:
        if function in dir(my_functions):
            function = getattr(my_functions, function)
            print(function())


runner()
runner('see_back', 'words')
runner('words')
runner('order_list')

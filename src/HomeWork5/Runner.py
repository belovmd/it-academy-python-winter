"""Оформите решение задач из прошлых домашних
 работ в функции. Напишите функцию runner.
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""
import my_functions


def runner(*functions):
    if not functions:
        functions = [item for item in dir(my_functions)
                     if not item.startswith(('__', 're'))]
    for function in functions:
        try:
            function = getattr(my_functions, function)
            print('Result of function {} is {}'.
                  format(function.__name__, function()))
        except AttributeError:
            print("Function {} doesn't exist".format(function))
        except ValueError:
            print('Incorrect input in function {}'.format(function.__name__))


runner()
runner('seeback', 'words')
runner('words')
runner('order_list')

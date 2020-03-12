"""Оформите решение задач из прошлых домашних
 работ в функции. Напишите функцию runner.
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""
import my_functions


def runner(*functions):
    if not functions:
<<<<<<< HEAD
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
=======
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
>>>>>>> 25601a1a117babf773e2c813d33b2d57cee0f252
runner('words')
runner('order_list')

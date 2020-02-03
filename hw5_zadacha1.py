"""
Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""
import hw5_func as hw5


def runner(*call_func):
    for el in call_func:
        a = getattr(hw5, el)
        a()
    if not call_func:
        for el in dir(hw5):
            if "_" not in el:
                a = getattr(hw5, el)
                a()


runner()

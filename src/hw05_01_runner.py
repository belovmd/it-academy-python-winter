"""
1.	Оформите решение задач из прошлых домашних
работ в функции. Напишите функцию runner.
a.	runner() – все фукнции вызываются по очереди
b.	runner(‘func_name’) – вызывается только функцию func_name.
c.	runner(‘func’, ‘func1’...) - вызывает все переданные функции

"""


import mymodule


def runner(*args):
    if not args:
        args = [elements for elements in
                dir(mymodule) if elements[:2] != '__']
    for attr in args:
        run_func = getattr(mymodule, attr)
        run_func()
        print('------------------')
print('-----------------------ВСЕ')
runner()
print('----------------------ОДНА')
runner('generator')
print('-----------------------ДВЕ')
runner('list_sort', 'generator')

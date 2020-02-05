# Оформите решение задач из прошлых домашних работ в функции. Напишите
# функцию runner.
# runner_a() – все фукнции вызываются по очереди
# runner_b(‘func_name’) – вызывается только функцию func_name.
# runner_c(‘func’, ‘func1’...) - вызывает все переданные функции

from my_functions import *

'''list of functions :
gen_dct() intersec(), semetric(), lenguagies(),
 words(), evklid()
'''


# print(globals())


def runner(*func):
    functions = {fun: path for fun, path in globals().items()
                 if not fun.startswith('_')}
    if not func:
        for i in functions:
            functions[i]()
    else:
        for i in [*func]:
            functions[i]()


runner()
# runner('num_intersect')
# runner('evklid', 'gen_dct')

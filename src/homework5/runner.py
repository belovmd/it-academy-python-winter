import allfunc

"""Оформите решение задач из прошлых домашних работ в функции. Напишите
функцию runner. (все станет проще когда мы изучим модули,
getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


def runner(*args):
    attrs = {attr: getattr(
             allfunc, attr) for attr in dir(allfunc) if
             callable(getattr(allfunc, attr))
             }
    if args:
        for fnc in args:
            print('Вызвана функция {}()\n'.format(fnc))
            attrs[fnc]()
            print('\n')
    else:
        for item in attrs.items():
            print('Вызвана функция {}()\n'.format(item[0]))
            item[1]()
            print('\n')


runner()
runner('pair_elements')
runner("set_words", 'evliklid')

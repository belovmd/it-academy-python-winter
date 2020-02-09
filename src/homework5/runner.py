import allfunc


def run_fnc(*args):
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


run_fnc("set_words", 'evliklid')

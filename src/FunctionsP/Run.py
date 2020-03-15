import functions


def runner(*func):

    if not func:
        lst_func = [el for el in dir(functions) if not el.startswith('__')]
    else:
        lst_func = [el for el in [*func]]
    for atr in lst_func:
        try:
            called = getattr(functions, atr)
            print(called())
        except AttributeError:
            print("Функция не найдена")


runner()
runner('FizzBuzz')
runner('FizzBuzz', 'InCommon')
runner("d")

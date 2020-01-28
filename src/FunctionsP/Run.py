import functions


def runner(*func):

    if not func:
        lst_func = [el for el in dir(functions) if "_" not in el]
    else:
        lst_func = [el for el in [*func] if el in dir(functions)]
    if lst_func:
        for atr in lst_func:
            called = getattr(functions, atr)
            print(called())
    else:
        print("Функция не найдена")

# Second variant
    if not func:
        lst_func = [el for el in dir(functions) if "_" not in el]
    else:
        lst_func = [el for el in [*func]]
    for atr in lst_func:
        if hasattr(functions, atr):
            called = getattr(functions, atr)
            print(called())
        else:
            print("Функция не найдена")


runner()
runner('FizzBuzz')
runner('FizzBuzz', 'InCommon')
runner("d")

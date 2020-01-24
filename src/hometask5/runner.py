# Напишите функцию runner.
# runner() – все фукнции вызываются по очереди
# runner(‘func_name’) – вызывает только функцию func_name.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции

import the_functions


def runner(*functions):
    if not functions:
        functions = [el for el in dir(the_functions) if el[:2]
                     not in ['re', '__']]
    for function in functions:
        called_function = getattr(the_functions, function)
        print('Вызов функции:', function)
        print('Результат:', called_function())


runner('words')
runner('words', 'look_back')
runner()

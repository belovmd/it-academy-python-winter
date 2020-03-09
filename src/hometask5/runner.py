# Напишите функцию runner.
# runner() – все фукнции вызываются по очереди
# runner(‘func_name’) – вызывает только функцию func_name.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции

import the_functions


def runner(*functions):
    if not functions:
        functions = [el for el in dir(the_functions)
                     if not el.startswith(('__', 're'))]
    for function in functions:
        try:
            called_function = getattr(the_functions, function)
            if callable(called_function):
                print('Function call:', function)
                print('Result:', called_function())
            else:
                raise AttributeError("This is something that I can't call")
        except (TypeError, AttributeError) as err:
            print('Error: {0}'.format(err))


runner('words2')
runner(1)
runner('non existing function')
runner('words', 'look_back')
runner(0)
runner('non existing function')
runner()

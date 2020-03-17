from Homework5 import task1


def runner(*functions):
    if not functions:
        functions = [func for func in dir(task1) if not func.startswith('__')]
    for func in functions:
        try:
            called_function = getattr(task1, func)
            if callable(called_function):
                print(func)
                called_function()
        except AttributeError:
            print(func)
            print('no such function')
        except TypeError:
            print('function call error')
        print()


runner()
runner('fizzbuzz')
runner('ddt', 'dct', 'check')

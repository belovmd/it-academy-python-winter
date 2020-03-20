# Создайте декоратор, который хранит результаты вызовы функции
# (за все время вызовов, не только текущий запуск программы)

from datetime import datetime


def dec(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('results.txt', 'a') as r:
            r.write('{}({})\n'.format(func.__name__,
                                      datetime.strftime(datetime.now(),
                                                        "%Y.%m.%d %H:%M:%S")))
            r.write('Result: {}\n'.format(result))

        return result

    return wrap


@dec
def gen_dct():
    dct = {key: key ** 3 for key in range(1, 30)}
    print(dct)
    return dct


gen_dct()

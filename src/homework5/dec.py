import datetime

"""Создайте декоратор, который хранит результаты вызова функции
(за все время вызовов, не только текущий запуск программы)

"""


def save_res(fnct):
    name = fnct.__name__

    def wrapper(*args, **kwargs):

        time_format = "%Y-%m-%d %H:%M:%S"
        now = datetime.datetime.now(tz=None)
        res = fnct(*args, **kwargs)
        output = (f'Вызванна функция {name}. '
                  f'Дата\\время вызова - {now: {time_format}}. '
                  f'Результат - {res}'
                  )
        with open('result.txt', 'a') as r:
            r.write(output)
        return output

    return wrapper


@save_res
def fib():
    rng = int(input('Введи длинну цепочки: '))
    a, b = 0, 1
    for i in range(rng):
        a, b = b, a + b
    return '{}-ое число фибоначчи = {}.\n'.format(rng, b)


print(fib())

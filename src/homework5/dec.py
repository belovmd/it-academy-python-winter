"""Создайте декоратор, который хранит результаты вызова функции
(за все время вызовов, не только текущий запуск программы)

"""


def save_res(fnct):
    def wrapper(*args, **kwargs):
        res = fnct(*args, **kwargs)
        with open('result.txt', 'a') as r:
            r.write(res)
        return res
    return wrapper


@save_res
def fib():
    rng = int(input('Введи длинну цепочки: '))
    a, b = 0, 1
    for i in range(rng):
        a, b = b, a + b
    return '{}-ое число фибоначчи = {}\n'.format(rng, b)


print(fib())

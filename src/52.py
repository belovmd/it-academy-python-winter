"""Создайте декоратор, который хранит результаты вызова функции
(за все время вызовов, не только текущий запуск программы)
"""


def result_function(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        with open('result.txt', 'a') as r:
            r.write(res)
        return res

    return wrapper


dct = {1: 1, 2: 1}


@result_function
def fib(n):
    if n in dct:
        return dct[n]
    dct[n] = fib(n - 1) + fib(n - 2)
    return dct[n]


fib_num = int(input("Enter number: "))
print(fib(fib_num))

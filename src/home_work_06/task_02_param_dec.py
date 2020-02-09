"""
Создайте декоратор, который вызывает задекорированную функцию
пока она не выполнится без исключений
(но не более n раз - параметр декоратора).
Если превышено количество попыток,
должно быть возбуждено исключение типа TooManyErrors
"""

import all_func
from functools import wraps


class TooManyErrors(Exception):
    pass


def error_count_dec(max_err_count):
    def result_decorator(func):
        func_err_count = {func: 0}
        func_run_count = {func: 0}

        @wraps(func)
        def wrapper(*args, **kwargs):
            name = func.__name__
            func_run_count[func] += 1
            try:
                if func_err_count[func] >= max_err_count:
                    raise TooManyErrors
            except TooManyErrors:
                return 'Func "{}" reached max errors'.format(name)
            else:
                try:
                    print('Func "{}" trying {} time'
                          .format(name, func_run_count[func]))
                    res = func(*args, **kwargs)
                    return res
                except Exception:
                    func_err_count[func] += 1
                    return 'Errors {}'.format(func_err_count[func])

        return wrapper

    return result_decorator


euklid = error_count_dec(3)(all_func.euklid)
fibonacci = error_count_dec(3)(all_func.fibonacci)

print(euklid('a', 'b'))
print(euklid('b', 'c'))
print(euklid('a', '1'))

print(euklid(30, 18))
print(euklid(360, 126))
print(euklid(400, 100))
print(euklid(56, 35))

print(fibonacci('a'))
print(fibonacci(5))
print(fibonacci(7))
print(fibonacci(10))

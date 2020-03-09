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
            params = [*args, *kwargs]
            for func_err_count[func] in range(max_err_count):
                try:
                    func_run_count[func] += 1
                    print('Func "{}" params {} trying {} time'
                          .format(name, params, func_run_count[func]))
                    res = func(*args, **kwargs)
                    return res
                except Exception:
                    func_err_count[func] += 1
                    print('Errors {}'.format(func_err_count[func]))
            else:
                try:
                    if func_err_count[func] >= max_err_count:
                        raise TooManyErrors
                except TooManyErrors:
                    func_run_count[func] = 0
                    res = 'Func "{}" params {} max errors'.format(name,
                                                                  params)
                    return res
        return wrapper
    return result_decorator


euklid = error_count_dec(3)(all_func.euklid)
fibonacci = error_count_dec(3)(all_func.fibonacci)

print(euklid('a', 'b'))
print(euklid(1, 'c'))
print(euklid(30, 18))

print(fibonacci('a'))
print(fibonacci(5))


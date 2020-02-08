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
    """
    @classmethod
    def __call__(cls, *args, **kwargs):
        print('Max calls for func "{}" reached'.format(*args))
    """
    pass


def param_dec(run_count):
    def result_decorator(func):
        func_err_count = {func: 0}

        @wraps(func)
        def wrapper(*args, **kwargs):
            func_err_count[func] += 1
            try:
                if func_err_count[func] > run_count:
                    raise TooManyErrors
            except TooManyErrors:
                return 'Max calls for func "{}" reached'.format(func.__name__)
                #return TooManyErrors.__call__(func.__name__)
            else:
                try:
                    print('Func "{}" trying {} time'.format(func.__name__, func_err_count[func]))
                    res = func(*args, **kwargs)
                    return res
                except Exception:
                    #func_err_count[func] += 1
                    return 'Error {}'.format(func_err_count[func])

        return wrapper

    return result_decorator


euklid = param_dec(5)(all_func.euklid)
fibonacci = param_dec(3)(all_func.fibonacci)

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

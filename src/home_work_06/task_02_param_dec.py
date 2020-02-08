"""
Создайте декоратор, который вызывает задекорированную функцию
пока она не выполнится без исключений
(но не более n раз - параметр декоратора).
Если превышено количество попыток,
должно быть возбуждено исключение типа TooManyErrors
"""


import all_func
from functools import wraps


def param_dec(run_count):
    def result_decorator(some_func):
        @wraps(some_func)
        def wrapper(*args, **kwargs):
            res = some_func(*args, **kwargs)
            with open('results.txt', 'a') as res_file:
                res_file.write('Function name: {}\n'.format(some_func.__name__))
                res_file.write('Result: {}\n\n'.format(res))
            return res
        return wrapper
    return result_decorator


euklid = param_dec(3)(all_func.euklid)


print(euklid(30, 18))
print(euklid(360, 126))
print(euklid(400, 100))
print(euklid(56, 35))

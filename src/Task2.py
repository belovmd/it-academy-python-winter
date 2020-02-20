"""Создайте декоратор, который вызывает задекорированную
функцию пока она не выполнится без исключений
(но не более n раз - параметр декоратора).
Если превышено количество попыток, должно быть
возбуждено исключение типа TooManyErrors"""
import random
from functools import wraps


def more_calls(calls):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for call in range(1, calls + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if call == calls:
                        raise

        return wrapper

    return dec


@more_calls(calls=5)
def func_to_decor():
    if random.randint(1, 20) > 10:
        raise IOError('TooManyErrors')
    else:
        print('calling example function')


func_to_decor()

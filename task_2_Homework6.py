""" Создайте декоратор,
    который вызывает задекорированную функцию
    пока она не выполнится без исключений
    (но не более n раз - параметр декоратора).
    Если превышено количество попыток,
    должно быть возбуждено исключение типа TooManyErrors

"""
import functools
import random



def retry(max_tries):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for n in range(1, max_tries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if n == max_tries:
                        raise

        return wrapper

    return decorator


@retry(max_tries=10)
def do_something_unreliable():
    """Do something unreliably."""
    if random.randint(0, 10) > 1:
        raise IOError("TooManyErrors")
    else:
        return "Awesome"


n = do_something_unreliable()
print(n)

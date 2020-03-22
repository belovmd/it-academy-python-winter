"""Создайте декоратор, который вызывает задекорированную
 функцию пока она не выполнится без исключений
 (но не более n раз - параметр декоратора).
  Если превышено количество попыток, должно быть
  возбуждено исключение типа TooManyErrors"""
import my_functions


class TooManyErrors(Exception):
    def __str__(self):
        return 'TooManyErrors'


def max_error(max_count_errors):
    def decorator(function):
        count_errors = 0

        def wrapper(*args, **kwargs):
            nonlocal count_errors
            count_run = max_count_errors
            while count_run:
                try:
                    return function(*args, **kwargs)
                except Exception:
                    count_errors += 1
                    count_run -= 1

                    print("You made {} mistakes in {}".
                          format(count_errors, function.__name__))
                finally:
                    try:
                        if count_errors >= max_count_errors:
                            count_errors = 0
                            raise TooManyErrors
                    except TooManyErrors:
                        return '{} in function {}'. \
                            format(TooManyErrors(), function.__name__)

        return wrapper

    return decorator


see_back = max_error(3)(my_functions.see_back)
get_ranges = max_error(3)(my_functions.get_ranges)
print(see_back(1, 2))
print(see_back(10, 'a'))
print(see_back(4, 2))
print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10, 11, 12]))
print(get_ranges([1, 2, 3, 'a']))
print(get_ranges([1, 2, 3, 4, 5, 'a', 7, 8, 9, 10]))



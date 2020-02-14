"""Создайте декоратор, который вызывает задекорированную
 функцию пока она не выполнится без исключений
 (но не более n раз - параметр декоратора).
  Если превышено количество попыток, должно быть
  возбуждено исключение типа TooManyErrors"""
import my_functions


def max_error(max_count_errors):
    def decorator(function):
        count_errors = 0

        def wrapper(*args, **kwargs):
            nonlocal count_errors
            try:
                function(*args, **kwargs)
            except Exception:
                count_errors += 1
                if count_errors > max_count_errors:
                    return 'TooManyErrors'
                else:
                    return "You made {} mistakes". \
                        format(count_errors)
            else:
                return function(*args, **kwargs)
        return wrapper
    return decorator


see_back = max_error(3)(my_functions.see_back)
get_ranges = max_error(3)(my_functions.get_ranges)
print(see_back(1, 'a'))
print(see_back(10, 15))
print(see_back(3, 'a'))
print(see_back(1, 2, 3))
print(see_back(15, 'a'))
print(get_ranges([1, 2, 3, 'a']))
print(get_ranges([1, 2, 3, 4, 5, 'a', 7, 8, 9, 10]))
print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10, 11, 12]))
print(get_ranges([1, 2, 3, 4, 5, 1, 'a', 2, 3, 4, 1, 3, 4, 5, 9]))
print(get_ranges([4, 7, 'a', 10]))
print(get_ranges([2, 3, 8, 'a', 9]))

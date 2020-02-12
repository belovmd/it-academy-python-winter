# Создайте декоратор, который вызывает задекорированную
# функцию пока она не выполнится без исключений (но не
# более n раз - параметр декоратора).
# Если превышено количество попыток,
# должно быть возбуждено исключение типа TooManyErrors

from functools import wraps
import the_functions_new


class TooManyErrors(Exception):
    def __init__(self, function_name):
        self.function_name = function_name

    def __str__(self):
        return 'TooManyErrors at {}'.format(self.function_name)


def error_decorator(critical_error_count):
    def count_decorator(function):
        function.__errors_count__ = 0
        function.__invocation_count__ = 0

        @wraps(function)
        def wrap(*args, **kwargs):
            name = function.__name__
            function.__invocation_count__ += 1
            try:
                if function.__errors_count__ > critical_error_count:
                    raise TooManyErrors(name)
            except TooManyErrors as result_of_function:
                return result_of_function
            else:
                try:
                    result = function(*args, **kwargs)
                    return 'Name: {},' \
                           ' result: {},' \
                           ' number of function calls: {}' \
                           ''.format(name, result,
                                     function.__invocation_count__)
                except Exception:
                    function.__errors_count__ += 1
                    return 'Name: {},' \
                           ' count function errors: {}' \
                           ''.format(name, function.__errors_count__)

        return wrap

    return count_decorator


if __name__ == '__main__':
    look_back = error_decorator(3)(the_functions_new.look_back)
    checkio = error_decorator(4)(the_functions_new.checkio)

    print(look_back('s', 12))
    print(look_back(40, 's'))
    print(look_back('s', 12))
    print(look_back(40, 's'))

    print(checkio("hello,world", "hello,earth"))
    print(checkio("one,two,three", "four,five,six"))
    print(checkio("one,two,three", 1))

    print(look_back(40, 12))
    print(look_back(58, 12))

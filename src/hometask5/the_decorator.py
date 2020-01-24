# Создайте декоратор, который хранит результаты вызовы
# функции (за все время вызовов, не только текущий запуск программы)

import the_functions


def file_logger_decorator(function):
    def wrap(*args, **kwargs):
        function_result = function(*args, **kwargs)
        with open('call_results.txt', 'a') as f:
            f.write('{}\n'.format(function.__name__))
            f.write('Result: {}\n\n'.format(function_result))
            f.write('{}\n'.format('-' * 10))
        return function_result
    return wrap


count_countries = file_logger_decorator(the_functions.count_countries)
look_back = file_logger_decorator(the_functions.look_back)
words = file_logger_decorator(the_functions.words)


look_back()

words()

count_countries()

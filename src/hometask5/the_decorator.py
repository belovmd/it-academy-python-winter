# Создайте декоратор, который хранит результаты вызовы
# функции (за все время вызовов, не только текущий запуск программы)

import datetime
import the_functions

now = datetime.datetime.now()


def file_logger_decorator(function):
    def wrap(*args, **kwargs):
        function_result = function(*args, **kwargs)
        with open('call_results.txt', 'a') as f:
            f.write('{}\n'.format(function.__name__))
            f.write('Result: {}\n'.format(function_result))
            f.write('Was called in: {}\n'.format(now.strftime
                                                 ("%d-%m-%Y %H:%M")))
            f.write('{}\n'.format('-' * 10))
        return function_result

    return wrap


count_countries = file_logger_decorator(the_functions.count_countries)
look_back = file_logger_decorator(the_functions.look_back)
words = file_logger_decorator(the_functions.words)

look_back()

words()

count_countries()

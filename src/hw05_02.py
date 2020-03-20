"""
2.	Создайте декоратор,
который хранит результаты
вызовы функции (за все время вызовов,
не только текущий запуск программы)
"""


from datetime import datetime
import mymodule


def log_dec(function):
    def wraper(*args, **kwargs):
        func_result = function(*args, **kwargs)
        with open('dec_logger.txt', 'a',  encoding='utf-8') as my_file:
            my_file.write('{} / '.format(datetime.now()))
            my_file.write('функция: {} / '.format(function.__name__))
            my_file.write('результат: {}\n'.format(func_result))
            my_file.write('{}\n'.format('*' * 50))
        return func_result
    return wraper


generator = log_dec(mymodule.generator)
list_sort = log_dec(mymodule.list_sort)
generator()
list_sort()
list_sort()
list_sort()
list_sort()
list_sort()
generator()
generator()
generator()

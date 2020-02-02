"""Создайте декоратор, который хранит результаты
вызовы функции (за все время вызовов,
не только текущий запуск программы)"""
import my_functions


def dec(func):
    def wrapper():
        with open('saves.txt', 'a') as my_saves:
            my_saves.write('{}: result - {}  \n'
                           .format(func.__name__, str(func())))
    return wrapper


order_list = dec(my_functions.order_list)
words = dec(my_functions.words)
see_back = dec(my_functions.see_back)

order_list()
words()
see_back()
order_list()
words()
see_back()

"""Создайте декоратор, который хранит результаты
вызовы функции (за все время вызовов,
не только текущий запуск программы)"""
import my_functions

dct_saves = {}


def dec(function):
    my_func_name = function.__name__

    def wrapper(*args, **kwargs):

        if my_func_name not in dct_saves:
            dct_saves.setdefault(my_func_name, [function(*args, **kwargs)])
        else:
            dct_saves[my_func_name].append(function(*args, **kwargs))
        return dct_saves

    return wrapper


order_list = dec(my_functions.order_list)
words = dec(my_functions.words)
see_back = dec(my_functions.see_back)

print(order_list())
print(words())
print(see_back())
print(order_list())
print(words())
print(see_back())

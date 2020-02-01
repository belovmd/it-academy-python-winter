"""
Создайте декоратор, который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)
"""

import random


def decorator(func_to_decorate):
    def wrapper():
        try:
            file = open('results_of_functions.txt', 'a')
            file.write(func_to_decorate() + '\n')
            file.close()
        except FileNotFoundError:
            print('No such file!')

    return wrapper()


@decorator
def usual_func():
    data = [random.randint(20, 30) for num in range(20)]
    return str(data)


@decorator
def usual_func_2():
    data = [random.randint(1, 10) for num in range(20)]
    return str(data)

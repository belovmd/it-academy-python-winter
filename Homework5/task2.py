# 2. Создайте декоратор, который хранит результаты вызовов функции
# (за все время вызовов, не только текущий запуск программы)

from datetime import datetime
from Homework5 import task1


def data_to_file(func):
    result = func()

    def wrapper():
        with open('file.txt', 'a') as f:
            f.write(str(datetime.now()) + '\n')
            f.write(func.__name__ + '\n')
            f.write(str(result) + '\n\n')
        return result

    return wrapper


gcd = data_to_file(task1.gcd)
dct = data_to_file(task1.dct)
list_to_tuple = data_to_file(task1.list_to_tuple)

gcd()
dct()
list_to_tuple()

"""Создайте декоратор, который вызывает задекорированную функцию пока она не
выполнится без исключений (но не более n раз - параметр декоратора). Если
превышено количество попыток, должно быть возбуждено исключение типа
TooManyErrors"""
import random


def Randomaiser(x=1, y=10, z=100):
    while z:
        z -= 1
        return (print(random.randint(x, y), end=" "))


def decor(quantity, fn):

    class TooManyErrors(Exception):
        pass

    def wraper_new(*args, **kwargs):
        qun_of_calls = quantity
        calls = 0
        while qun_of_calls:
            fn(*args, **kwargs)
            qun_of_calls -= 1
            calls += 1
        else:
            raise TooManyErrors(f'{fn.__name__} was called more than {calls} '
                                f'calls')

    return wraper_new


Randomaiser = decor(50, Randomaiser)
Randomaiser()

"""Создайте декоратор, который вызывает задекорированную функцию пока она не
выполнится без исключений (но не более n раз - параметр декоратора). Если
превышено количество попыток, должно быть возбуждено исключение типа
TooManyErrors"""
import random


def QQQ(x=1, y=10, z=100):
    while z:
        z -= 1
        return (print(random.randint(x, y), end=" "))


def decor(fn):
    def wraper_new(*args, **kwargs):
        qun_of_call = 50
        while qun_of_call:
            fn(*args, **kwargs)
            qun_of_call -= 1
        else:
            raise Exception('TooManyError')

    return wraper_new


QQQ = decor(QQQ)
QQQ()
QQQ()

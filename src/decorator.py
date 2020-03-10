"""
Создайте декоратор, который вызывает
задекорированную функцию пока она не
выполнится без исключений
(но не более n раз - параметр декоратора).
Если превышено количество попыток,
должно быть возбуждено исключение типа TooManyErrors

"""


def count_errors(num):
    attemp = num

    def decorator(func):
        def wrapper(*args, **kw):
            nonlocal attemp
            while attemp:
                try:
                    resault = func(*args, **kw)
                    return resault
                except Exception as ex:
                    attemp -= 1
                    return ex.args[0]
            else:
                return Exception('TooManyErrors')
        return wrapper
    return decorator


@count_errors(3)
def my_func(a, b):
    return a / b


if __name__ == '__main__':
    print(my_func(1, 2))
    print(my_func(2, 2))
    print(my_func(3, 'a'))
    print(my_func(3, 0))
    print(my_func(3, 0))
    print(my_func(3, 0))
    print(my_func(4, 2))








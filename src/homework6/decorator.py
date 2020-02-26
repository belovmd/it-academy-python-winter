"""Создайте декоратор, который вызывает задекорированную функцию
пока она не выполнится без исключений (но не более n раз - параметр
декоратора). Если превышено количество попыток, должно быть возбуждено
исключение типа TooManyErrors

"""


def decorator(errors):

    def dec(func):
        def wrapper(*args, **kwargs):
            nonlocal errors
            try:
                result = func(*args, **kwargs)
            except Exception:
                while errors:
                    errors -= 1
                    return 'Something wrong'
                else:
                    return 'TooManyErrors'
            else:
                return result
        return wrapper

    return dec


@decorator(3)
def division(a, b):
    return a / b


if __name__ == '__main__':
    print(division(6, 0))
    print(division(0, 5))
    print(division(7, 0))
    print(division(4, 4))
    print(division(0, '3'))
    print(division('7', 3))

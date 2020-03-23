class TooManyErrors(Exception):
    pass


def too_many_errors(n):
    num = n

    def decorator(function):
        def wrapper(*args):
            nonlocal num
            while num:
                try:
                    result = function(*args)
                    return result
                except Exception as exception:
                    num -= 1
                    return exception
            else:
                try:
                    raise TooManyErrors
                except TooManyErrors:
                    print('TooManyErrors')
                    exit(0)

        return wrapper

    return decorator


@too_many_errors(2)
def func(a, b):
    return a / b


print(func(1, 'abc'))
print(func(2, 2))
print(func(1, 5, 'xyz'))
print(func(2.5, 2))
print(func(1, 0))
print(func(456, 123))

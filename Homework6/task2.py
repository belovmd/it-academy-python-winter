def too_many_errors(n):
    num = n
    without_exception = False

    def decorator(function):
        def wrapper(*args):
            nonlocal num, without_exception
            while not without_exception:
                while num:
                    try:
                        result = function(*args)
                        without_exception = True
                        return result

                    except Exception as exception:
                        num -= 1
                        return exception
                else:
                    return Exception('TooManyErrors')
            else:
                exit(0)

        return wrapper

    return decorator


@too_many_errors(3)
def func(a, b):
    return a / b


print(func(1, 'abc'))
print(func(1, 0))
print(func(1, 5, 'xyz'))
print(func(2.5, 2))
print(func(2, 2))
print(func(456, 123))

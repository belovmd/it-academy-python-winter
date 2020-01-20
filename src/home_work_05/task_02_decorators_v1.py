def result_decorator(some_func):
    result = []
    def wrapper(*args, **kwargs):
        nonlocal result
        result.append(some_func(*args, **kwargs))
        return result
    return wrapper


@result_decorator
def multiplier(first_num, second_num):
    return first_num * second_num


print(multiplier(3, 5))
print(multiplier(2, 8))
print(multiplier(4, 9))

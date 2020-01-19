import task_01_all_func

def dec_result(some_func):
    def wrapper(*args, **kwargs):
        print('inside decorator')
        result = some_func(*args, **kwargs)
        return result
    return wrapper

@dec_result
euklid
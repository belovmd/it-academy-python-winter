# Создайте декоратор, который хранит результаты вызовы
# функции (за все время вызовов, не только текущий запуск программы)


import my_func
from datetime import datetime
from functools import wraps


def result_decorator(some_func):
    @wraps(some_func)
    def wrapper(*args, **kwargs):
        res = some_func(*args, **kwargs)
        current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('results.txt', 'a') as file_result:
            file_result.write('Имя функции: {}\n'.format(some_func.__name__))
            file_result.write('Время вызова: {}\n'.format(current_date_time))
            file_result.write('Результат вызова: {}\n\n'.format(res))
        return res
    return wrapper


euklid = result_decorator(my_func.euklid)
diff_words = result_decorator(my_func.diff_words)
languages = result_decorator(my_func.languages)
pair_elem = result_decorator(my_func.pair_elem)


euklid(30, 18)
euklid(360, 126)

diff_words('aaa \n\nbbb\n aaa   cc  vvv\nbbb      ddd')
diff_words('ff a \n\nb b\n aaa vvv  ed  vvv\n \n  \nbbb      aaa')

languages('rus, eng', 'rus, ger', 'rus, jap, ital')
languages('rus, eng, fra', 'rus, ger, eng', 'rus, jap, eng')

pair_elem('1 1 1 2 2 2 1')
pair_elem('5 5 5 7 7')

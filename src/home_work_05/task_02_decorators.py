"""
Создайте декоратор, который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)
"""

import all_func
from functools import wraps


def result_decorator(some_func):
    @wraps(some_func)
    def wrapper(*args, **kwargs):
        res = some_func(*args, **kwargs)
        with open('results.txt', 'a') as res_file:
            res_file.write('Function name: {}\n'.format(some_func.__name__))
            res_file.write('Result: {}\n\n'.format(res))
        return res
    return wrapper


euklid = result_decorator(all_func.euklid)
diff_words = result_decorator(all_func.diff_words)
languages = result_decorator(all_func.languages)
pair_elem = result_decorator(all_func.pair_elem)


euklid(30, 18)
euklid(360, 126)

diff_words('aaa \n\nbbb\n aaa   cc  vvv\nbbb      ddd')
diff_words('ff a \n\nb b\n aaa vvv  ed  vvv\n \n  \nbbb      aaa')

languages('rus, eng', 'rus, ger', 'rus, jap, ital')
languages('rus, eng, fra', 'rus, ger, eng', 'rus, jap, eng')

pair_elem('1 1 1 2 2 2 1')
pair_elem('5 5 5 7 7')

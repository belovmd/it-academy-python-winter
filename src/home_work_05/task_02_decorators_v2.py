"""
Создайте декоратор, который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)
"""

import all_func


def result_decorator(some_func):
    def wrapper(*args, **kwargs):
        result = some_func(*args, **kwargs)
        with open('results.txt', 'a') as res_file:
            res_file.write('Function name: {}\n'.format(some_func.__name__))
            res_file.write('Result: {}\n\n'.format(some_func(*args, **kwargs)))
        return result
    return wrapper


euklid = result_decorator(all_func.euklid)
diff_words = result_decorator(all_func.diff_words)
cities = result_decorator(all_func.cities)
what_country = result_decorator(all_func.what_country)
languages = result_decorator(all_func.languages)

euklid(30, 18)
euklid(360, 126)

diff_words('aaa \n\nbbb\n aaa   cc  vvv\nbbb      ddd')
diff_words('ff a \n\nb b\n aaa vvv  ed  vvv\n \n  \nbbb      aaa')

dct = cities('Russia Moscow Petersburg Novgorod Kaluga', 'Ukraine Kiev Donetsk Odessa')
what_country(dct, 'Odessa', 'Moscow', 'Minsk')
dct = cities('Belarus Minsk Brest Gomel Grodno')
what_country(dct, 'Odessa', 'Moscow', 'Minsk')

languages('rus, eng', 'rus, ger', 'rus, jap, ital')
languages('rus, eng, fra', 'rus, ger, eng', 'rus, jap, eng')

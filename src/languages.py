"""Каждый из N школьников некоторой школы знает Mi языков. Определите,
какие языки знают все школьники и языки, которые знает хотя бы один из школьников.

Входные данные
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
содержащих названия языков, которые знает i-й школьник.
Пример:
3          - N количество школьников
2          - M1 количество языков первого школьника
Russian    - языки первого школьника
English
3          - M2 количество языков второго школьника
Russian
Belarusian
English
3
Russian
Italian
French

Выходные данные
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков. Затем - количество языков,
которые знает хотя бы один школьник, на следующих строках - список таких языков.
"""

import copy
count_schoolboys = int(input('Введите количество школьников: '))
lst_languages = {}
for i in range(1, count_schoolboys + 1):
    languages = set(input('Введите язык для {} школьника: '.format(i)) for j in range(int(input('Введите количество языков: '))))
    lst_languages[i] = languages
copy_lst_languages = copy.deepcopy(lst_languages)
i = 1
while i != len(lst_languages):
    lst_languages[1].intersection_update(lst_languages[i + 1])
    copy_lst_languages[1].update(copy_lst_languages[i + 1])
    i += 1
print('Языков знают все школьники: {}'.format(len(lst_languages[1])))
print(*lst_languages[1])
print('Языков знают хотя бы один школьник: {}'.format(len(copy_lst_languages[1])))
print(*copy_lst_languages[1])

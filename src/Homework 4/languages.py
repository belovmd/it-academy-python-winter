"""Каждый из N школьников некоторой школы знает Mi языков. Определите,
какие языки знают все школьники и языки, которые знает хотя бы один из
школьников.

Входные данные
Первая строка входных данных содержит количество школьников N. Далее
идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих
названия языков, которые знает i-й школьник.
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
Начиная со второй строки - список таких языков. Затем - количество
языков, которые знает хотя бы один школьник, на следующих
строках - список таких языков.

"""


# Цикл опроса о количестве языков.
def lang_fnc(dis_qlt):
    while dis_qlt:
        lang_count = int(input('Сколько языков знает {} школьник: '
                               .format(disciples - (dis_qlt - 1))))
        lang_inp(lang_count)
        dis_qlt -= 1


# Цикл ввода языков после получения количества.
def lang_inp(lang_count):
    while lang_count:
        lang_type = input('>>> ')
        lang.setdefault(lang_type, 0)
        lang[lang_type] += 1
        lang_count -= 1


# Цикл печати языков, какие знаю все ученики и какие только единицы.
def print_lang(max_, min_):
    for val in max_, min_:
        print(len(lang_max[val]))
        for unit in lang_max[val]:
            print(unit)


disciples = int(input('Сколько учеников? '))
lang = {}
lang_fnc(disciples)
# Перепаковываем словарь в словарь с вложеными списками
lang_max = {}
for lng, qlt in lang.items():
    lang_max.setdefault(qlt, [])
    lang_max[qlt].append(lng)
print_lang(disciples, 1)

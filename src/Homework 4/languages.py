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
def how_knows_lang(disciples_quantity):
    while disciples_quantity:
        lang_count = int(input('Сколько языков знает {} школьник: '
                         .format(disciples - (disciples_quantity - 1)))
                         )
        lang_input(lang_count)
        disciples_quantity -= 1


# Цикл ввода языков после получения количества.
def lang_input(lang_count):
    while lang_count:
        lang_type = input('>>> ')
        languages.setdefault(lang_type, 0)
        languages[lang_type] += 1
        lang_count -= 1


# Цикл печати языков, какие знаю все ученики и какие только единицы.
def print_lang(max_lang, min_lang=1):
    for value in max_lang, min_lang:
        print(len(known_languages[value]))
        for unit in known_languages[value]:
            print(unit)


disciples = int(input('Сколько учеников? '))
languages = {}
how_knows_lang(disciples)
# Перепаковываем словарь в словарь с вложеными списками
known_languages = {}
for language, qualtity in languages.items():
    known_languages.setdefault(qualtity, [])
    known_languages[qualtity].append(language)
print_lang(disciples, )

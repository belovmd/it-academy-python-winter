"""
Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки
знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N. Далее идет N
чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков,
которые знает i-й школьник. Пример:
3 - N количество школьников
2 - M1 количество языков первого школьника
Russian - языки первого школьника
English
3 - M2 количество языков второго школьника
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
которые знает хотя бы один школьник, на следующих строках - список таких
языков.
"""

number_pupils = int(input())
lst_of_pupils = []
dct_of_languages = {}
for i in range(number_pupils):
    number_lang = int(input())
    for i in range(number_lang):
        lst_of_pupils.append(input())
for symbol in lst_of_pupils:
    dct_of_languages[symbol] = dct_of_languages.get(symbol, 0) + 1
count_all = 0
count_one = 0
for symbol in dct_of_languages:
    if dct_of_languages.get(symbol) == number_pupils:
        count_all += 1
    else:
        count_one += 1
if count_all > 0:
    print(count_all)
    for symbol in dct_of_languages:
        if dct_of_languages.get(symbol) == number_pupils:
            print(symbol)
else:
    print("У школьников нет общих языков")
if count_one > 0:
    print(count_one)
    for symbol in dct_of_languages:
        if dct_of_languages.get(symbol) != number_pupils:
            print(symbol)

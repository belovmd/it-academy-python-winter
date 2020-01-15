"""
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.

---Входные данные
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
содержащих названия языков, которые знает i-й школьник.
---Пример:
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

---Выходные данные
В первой строке выведите количество языков,
которые знают все школьники.
Начиная со второй строки - список таких языков.
Затем - количество языков,
которые знает хотя бы один школьник,
на следующих строках - список таких языков.
"""


schoolchilds = {}
count_schoolchilds = int(input('Количество школьников: '))
for numm in range(count_schoolchilds):
    count_languages = int(input('Количество языков  школьника:'))
    schoolchilds[numm] = []
    for numm2 in range(count_languages):
        schoolchilds[numm].append(input('язык школьника: '))
for sets in schoolchilds.values():
    for_all_schoolchilds = set.intersection(*[set(leng) for leng
                                              in schoolchilds.values()])
    for_any_schoolchilds = set.union(*[set(leng) for leng
                                       in schoolchilds.values()])
if not for_all_schoolchilds:
    print('Нет общих языков')
else:
    print('Количество языков, которые знают '
          'все школьники:', len(for_all_schoolchilds))
    for leng01 in for_all_schoolchilds:
        print(leng01)
if for_any_schoolchilds:
    print('Количество языков, которые знает хотя '
          'бы один школьник:', len(for_any_schoolchilds))
    for leng02 in for_any_schoolchilds:
        print(leng02)

# Языки
# Каждый из N школьников некоторой школы знает Mi
# языков. Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.
# Входные данные
# Первая строка входных данных содержит количество школьников N.
# Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих
# названия языков, которые знает i-й школьник. Пример:
# 3          - N количество школьников
# 2          - M1 количество языков первого школьника
# Russian    - языки первого школьника
# English
# 3          - M2 количество языков второго школьника
# Russian
# Belarusian
# English
# 3
# Russian
# Italian
# French


# Выходные данные
# В первой строке выведите количество языков, которые знают все школьники.
# Начиная со второй строки - список таких языков. Затем - количество
# языков, которые знает хотя бы один школьник, на следующих
# строках - список таких языков.

pupils = {}
languages = set()
n = int(input("Enter quantity of pupils: "))
for pupil in range(1, n + 1):
    quantity_languages = int(input('Enter, how much languages '
                                   'knows ' + str(pupil) + ' pupil: '))
    for i in range(1, quantity_languages + 1):
        language = str(input('His ' + str(i) + ' language is : '))
        languages.add(language)
    pupils[pupil] = languages.copy()
    languages.clear()
print(pupils)

for i in pupils:
    if i < 2:
        languages = pupils[i] & pupils[i + 1]
    else:
        languages &= pupils[i]
print('All pupils knows ' + str(len(languages)) + ' languages: ')
for i in languages:
    print(i)
for i in pupils:
    languages.update(pupils[i])
print(str(len(languages)) + ' languages know least one pupil it is: ')
for i in languages:
    print(i)

# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.

# Входные данные
# Первая строка входных данных содержит количество школьников N.
# Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
# содержащих названия языков, которые знает i-й школьник.

# Пример:
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
# В первой строке выведите количество языков, которые знают
# все школьники. Начиная со второй строки - список таких языков.
# Затем - количество языков, которые знает хотя бы один школьник,
# на следующих строках - список таких языков.

students = {}
count_students = int(input('Введите количество школьников: '))

for i in range(count_students):
    count_languages = int(input('Введите количество'
                                ' языков школьника: '))
    students[i] = []
    for _ in range(count_languages):
        students[i].append(input('Введите язык: '))

for_all_students = list(set.intersection(*[set(value) for value
                                           in students.values()]))
if not for_all_students:
    print('Языков, которые знают все школьники, нет')
else:
    print('Количество языков, которые'
          ' знают все школьники: ' + str(len(for_all_students)))
    print('Эти языки знают все школьники: ')
    print("\n".join(for_all_students))

just_for_one = list(set.union(*[set(value) for value
                                in students.values()]))
print('Это количество языков, которые знает хотя бы'
      ' один школьник: ' + str(len(just_for_one)))
print('Эти языки знает хотя бы один школьник: ')
print("\n".join(just_for_one))

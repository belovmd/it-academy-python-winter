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
languges = []
p = set()
o = set()

n = int(input("Enter quantity of pupils: "))
for pupil in range(1, n + 1):
    quantity_languages = int(input('Enter, how much languages '
                                   'knows ' + str(pupil) + ' pupil: '))
    for i in range(1, quantity_languages + 1):
        i = str(input('His ' + str(i) + ' language is : '))
        languges.append(i)
    pupils[pupil] = {a for a in languges}
    languges.clear()
# print(pupils)   # general list of pupils

# count quantity of pupils:
s = pupils.keys()
s = len(s)

# lang which all pupils know :
for i in range(1, s + 1):
    if i < s:
        p = pupils[i] & pupils[i + 1]
    else:
        p &= pupils[i]

print('All pupils knows ' + str(len(p)) + ' languages: ')
for i in p:
    print(i)

#  all lang which least one pupil know
for i in range(1, s + 1):
    o.update(pupils[i])

print(str(len(o)) + ' languages know least one pupil it is: ')
for i in o:
    print(i)

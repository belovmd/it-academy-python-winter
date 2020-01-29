# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.
import copy
count_students = int(input('Введите количество школьников: '))
lst_languages = {}
for student in range(1, count_students + 1):
    languages = set(input('Введите язык для {}-го школьника: '.format(student))
                    for j in range(int(input('Введите количество языков: '))))
    lst_languages[student] = languages
copy_lst_languages = copy.deepcopy(lst_languages)
i = 0
while i != len(lst_languages):
    lst_languages[1].intersection_update(lst_languages[i + 1])
    copy_lst_languages[1].update(copy_lst_languages[i + 1])
    i += 1
print('Количество языков, которые знают все школьники: {}'.format(len(lst_languages[1])))
print(*lst_languages[1])
print('Количество языков, которые знает хотя бы один школьник: {}'.format(len(copy_lst_languages[1])))
print(*copy_lst_languages[1])

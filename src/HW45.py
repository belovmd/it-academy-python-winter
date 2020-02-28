# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.
import copy

count_students = int(input('Введите количество школьников: '))
lst_lang = {}
for student in range(1, count_students + 1):
    languages = set(input('Введите язык для {}-го школьника: '.format(student))
                    for language in range(int(input('Введите количество языков: '))))
    lst_lang[student] = languages
copy_lst_lang = copy.deepcopy(lst_lang)
count_laguage = 0
while count_laguage != len(lst_lang):
    lst_lang[1].intersection_update(lst_lang[count_laguage + 1])
    copy_lst_lang[1].update(copy_lst_lang[count_laguage + 1])
    count_laguage += 1
print('Количество языков, которые знают все школьники: '
      '{}'.format(len(lst_lang[1])))
print(*lst_lang[1])
print('Количество языков, которые знает хотя бы один школьник:'
      ' {}'.format(len(copy_lst_lang[1])))
print(*copy_lst_lang[1])

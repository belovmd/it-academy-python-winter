"""
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
"""

langs = [{input('Введите язык\n') for num_lang in
          range(int(input('Введите кол-во языков\n')))}
         for num_stud in range(int(input('Введите кол-во школьников\n')))]

lang_all = set.intersection(*langs)
lang_one = set.union(*langs)
print('Кол-во языков, которые знают все', len(lang_all))
print(*lang_all)
print('Кол-во языков, которые знает хотя бы один', len(lang_one))
print(*lang_one)

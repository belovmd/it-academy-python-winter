"""
Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки
знают все школьники и языки, которые знает хотя бы один из школьников.
"""
school_child_count = int(input("Please enter the number of school_child:"))
# создание словаря, в котором ключ - условный порядковый номер ученика,
# значение - список языков, которые он знает
school_child_languages = {}
# итерация по каждому школьнику
for school_child_index in range(school_child_count):
    school_child_languages[school_child_index] = []
    language_count = int(input("Enter the number languages for " + str(school_child_index + 1) + " schoolchild:"))
    # создание списка языков, которые знает школьник
    for language_ind in range(language_count):
        school_child_languages[school_child_index].append(input("Enter the " + str(language_ind + 1) + " language:"))
# создаем список языков, которые знают все школьники
intersection_languages = set()
# по аганлогии, создаем список языков, которые знает хотя бы один школьник
update_languages = set()
# итерируемся по паре (школьник, [изученные языки])
for child, languages_lst in school_child_languages.items():
    # добавляем значения в первое множество, когда оно пустое
    # и выполняем пересечение,если в множестве уже есть значения
    intersection_languages.intersection_update(languages_lst) if intersection_languages else \
        intersection_languages.update(languages_lst)
    # постоянно обновляем второй список списком языков ученика на каждой итерации
    # для добавления новых языков
    update_languages.update(languages_lst)
print(len(intersection_languages))
for language in intersection_languages:
    print(language)
print(len(update_languages))
for language in update_languages:
    print(language)

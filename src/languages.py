"""
Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки
знают все школьники и языки, которые знает хотя бы один из школьников.
"""
school_child_count = int(input("Please enter the number of school_child:"))
# создание словаря, в котором ключ - условный порядковый номер ученика,
# значение - список языков, которые он знает
child_languages = {}
# итерация по каждому школьнику
for child in range(school_child_count):
    child_languages[child] = []
    language_count = int(input("Enter the number languages for " +
                               str(child + 1) + " schoolchild:"))
    # создание списка языков, которые знает школьник
    for language in range(language_count):
        child_languages[child].append(input("Enter the " +
                                            str(language + 1) +
                                            " language:"))
# создаем список языков, которые знают все школьники
common_languages = set()
# по аганлогии, создаем список языков, которые знает хотя бы один школьник
update_languages = set()
# итерируемся по паре (школьник, [изученные языки])
for child, languages_lst in child_languages.items():
    # добавляем значения в первое множество, когда оно пустое
    # и выполняем пересечение,если в множестве уже есть значения
    common_languages.intersection_update(languages_lst) if common_languages\
        else common_languages.update(languages_lst)
    # постоянно обновляем второй список списком языков ученика
    # на каждой итерации
    # для добавления новых языков
    update_languages.update(languages_lst)
print(len(common_languages))
for language in common_languages:
    print(language)
print(len(update_languages))
for language in update_languages:
    print(language)

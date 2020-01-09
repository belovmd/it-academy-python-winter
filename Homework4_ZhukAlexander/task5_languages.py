"""
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники
и языки, которые знает хотя бы один из школьников.

Входные данные
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
содержащих названия языков, которые знает i-й школьник.
Пример:
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

"""

student_list = [{input("Язык школьника: ") for qnt_languages in
                range(int(input("Количество языков: ")))}
                for qnt_students in range(int(input("Количество "
                                                    "школьников: ")))]
# print(student_list)
all_know = set.intersection(*student_list)
somebody_know = set.union(*student_list)
print("Языки, которые знают все: ", len(all_know), ":", all_know)
print("Языки, которые знает хотя "
      "бы один из школьников: ", len(somebody_know), ":", somebody_know)

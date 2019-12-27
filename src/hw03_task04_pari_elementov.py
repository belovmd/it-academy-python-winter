"""
Дан список чисел. Посчитайте, сколько в нем пар элементов,
 равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


str01 = input('Введите список чисел через пробел:')
list01 = str01.split()
count_pari = 0
list02 = []
print('колличество эемеентов: ', len(list01))
print(list01)
for element01 in range(len(list01)):
    for element02 in range(element01 + 1, len(list01)):
        if list01[element01] == list01[element02]:
            count_pari += 1
            list02.append([list01[element01], list01[element02]])
print(count_pari)
if list02:
    print(list02)
else:
    print('Нет одинаковых пар!')

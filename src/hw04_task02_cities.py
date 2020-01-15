"""
- Города
Дан список стран и городов каждой страны.
Затем даны названия городов.

Для каждого города укажите, в какой стране он находится.

- Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны.

В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов,
перечисленных выше.
- Выходные данные
Для каждого из запроса выведите название страны,
в котором находится данный город.
- Примеры
Входные данные
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
3
Odessa
Moscow
Novgorod

Выходные данные
Ukraine
Russia
Russia
"""


strani = {}
count_strani = int(input('Введите количество стран: '))
for numm in range(count_strani):
    strana, *goroda = input('страна город город ......:').split()
    strani[strana] = goroda
count_goroda = int(input('Введите количество городов: '))
found_strana = []
for numm in range(count_goroda):
    city = input('Введите город:')
    for ctrana, goroda in strani.items():
        if city in goroda:
            found_strana.append(ctrana)
for strana in found_strana:
    print(strana)

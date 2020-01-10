"""Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк,
 каждая строка начинается с названия страны, затем идут
 названия городов этой страны. В следующей строке записано число M,
 далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны,
в котором находится данный город.

Примеры:

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

list_cities = [input().split() for l in range(int(input()))]
dct_cities = {}
for i in list_cities:
    dct_cities[i[0]] = i[1:]
print(dct_cities)
my_cities = [input() for l in range(int(input()))]
for country in dct_cities:
    for city in my_cities:
        if city in dct_cities[country]:
            print(country)

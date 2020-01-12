"""
Дан список стран и городов каждой страны. Затем даны названия городов. Для
каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк, каждая
строка начинается с названия страны, затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M запросов — названия каких-то
M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный
город.
Примеры
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

number_countries = int(input())
dct_1 = {}
for i in range(number_countries):
    lst_1 = [str(el) for el in input().split()]
    for symbol in lst_1[1::1]:
        if dct_1.get(symbol) is None:
            dct_1[symbol] = lst_1[0]
        else:
            # Check common cities. Example Brest in France and Belarus
            dct_1[symbol] = dct_1.get(symbol) + " " + lst_1[0]
number_cities = int(input())
lst_2 = []
for i in range(number_cities):
    lst_2.append(input())
for el in range(len(lst_2)):
    print(dct_1.get(lst_2[el]))

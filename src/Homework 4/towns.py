"""Дан список стран и городов каждой страны. Затем даны названия
городов. Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк,
каждая строка начинается с названия страны, затем идут названия
городов этой страны. В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится
данный город.
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


# Разбираем строку на города:страну, добавляем в словарь
def get_towns(countries_q, ):
    while countries_q:
        input_towns = input('Введи строку: ').split(' ')
        towns.update({unit: input_towns[0] for unit in input_towns[1:]})
        countries_q -= 1


# Проверяем наличие города в словаре и выводим его страну
def check_town(towns_q, ):
    countries = ''
    while towns_q:
        countries += towns.get(input('Введи название города: '),
                               'Такого города нет в списке') + '\n'
        towns_q -= 1
    return countries


towns = {}
get_towns(int(input('Введи количество стран: ')))
print(check_town(int(input('Сколько городов проверяем? '))))

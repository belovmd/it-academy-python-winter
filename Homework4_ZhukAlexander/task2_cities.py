"""
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.

Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны.
В следующей строке записано число M,
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

country_cities = {}
qnt_country = int(input("Количество стран: "))
for i in range(qnt_country):
    country, *cities = input("Введите страну и её "
                             "города через пробел: ").split()
    for city in cities:
        country_cities[city] = country
print(country_cities)

qnt_cities = int(input("Количество городов: "))
for j in range(qnt_cities):
    city = input("Введите город: ")
    print(country_cities.get(city, "Город не в списке"))

# Дан список стран и городов каждой страны.
# Затем даны названия городов. Для каждого города укажите,
# в какой стране он находится.

# Входные данные
# Программа получает на вход количество стран N. Далее идет N строк,
# каждая строка начинается с названия страны, затем идут названия
# городов этой страны. В следующей строке записано число M,
# далее идут M запросов — названия каких-то M городов,
# перечисленных выше.

# Выходные данные
# Для каждого из запроса выведите название страны,
# в котором находится данный город.

# Примеры
# Входные данные
# 2
# Russia Moscow Petersburg Novgorod Kaluga
# Ukraine Kiev Donetsk Odessa
# 3
# Odessa
# Moscow
# Novgorod

# Выходные данные
# Ukraine
# Russia
# Russia

countries = {}
count_countries = int(input('Введите количество стран: '))
for _ in range(count_countries):
    country, *cities = input().split()
    countries[country] = cities

count_cities = int(input('Введите количество городов: '))

for _ in range(count_cities):
    city = input()
    for country, cities in countries.items():
        if city in cities:
            print(country)

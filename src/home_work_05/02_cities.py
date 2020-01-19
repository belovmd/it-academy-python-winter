"""
Дан список стран и городов каждой страны.
Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
"""

cities = {}
for num_countries in range(int(input('Введите кол-во стран\n'))):
    country, *city_list = input('Введите страну и города\n').split()
    cities.update({city: country for city in city_list})

for num_cities in range(int(input('Введите кол-во городов\n'))):
    print(cities.get(input('Введите город\n'), 'Такого города нет'))

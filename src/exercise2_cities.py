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

countr = {}
count_countr = int(input('Please, enter the number of countries: '))
for _ in range(count_countr):
    country, *cit = input().split()
    countr[country] = cit

count_cit = int(input('Please, enter the number of cities: '))

for _ in range(count_cit):
    city = input()
    for country, cit in countr.items():
        if city in cit:
            print(country)

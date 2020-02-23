# Дан список стран и городов каждой страны
# Затем даны названия городов.
# Для каждого города укажите,
# в какой стране он находится
# Программа получает на вход количество стран N.
# Далее идет N строк, каждая строка начинается
# с названия страны, затем идут названия городов этой страны.
# В следующей строке записано число M, далее идут M запросов —
# названия каких-то M городов, перечисленных выше.

country_num = int(input())
catalog1 = {}
for i in range(country_num):
    country_name, *cities = input().split()
    catalog1[country_name] = cities

num_req = int(input())
list_request = []

for i in range(num_req):
    list_request.append(input())

for element in list_request:
    for country_name, city_name in catalog1.items():
        if element in city_name:
            print(country_name)

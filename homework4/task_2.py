# Дан список стран и городов каждой страны. Затем даны названия городов. Для
# каждого города укажите, в какой стране он находится.
# Входные данные
# Программа получает на вход количество стран N. Далее идет N строк, каждая
# строка начинается с названия страны, затем идут названия городов этой
# страны. В следующей строке записано число M, далее идут M
# запросов — названия каких-то M городов, перечисленных выше.
# Выходные данные
# Для каждого из запроса выведите название страны, в котором
# находится данный город.
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
n = int(input("Enter quantity of countries: "))
list_countries = {}
list_cities = []

for i in range(1, n + 1):
    i = str(input('Enter ' + str(i) + ' list of country and cities: '))
    i = i.split()
    list_countries[i[0]] = {a for a in i[1:]}

    # print(list_countries)

m = int(input("Enter how many cities do you want find ? "))
for i in range(1, m + 1):
    i = str(input('Enter ' + str(i) + '  city: '))
    list_cities.append(i)
# print(list_cities)

for j in list_cities:
    for i in list_countries:
        if j in list_countries[i]:
            print(i)

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
    string_of_words = str(input('Enter ' + str(i) + ' list of country '
                                                    'and cities: '))
    list_of_words = string_of_words.split()
    list_countries[list_of_words[0]] = {a for a in list_of_words[1:]}
m = int(input("Enter how many cities do you want find ? "))
for i in range(1, m + 1):
    list_cities.append(str(input('Enter ' + str(i) + '  city: ')))

for j in list_cities:
    for i in list_countries:
        if j in list_countries[i]:
            print(i)

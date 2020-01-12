# Города
# Дан список стран и городов каждой страны.
# Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.

f = open('cities.txt')

dct_cities = {}
for i in range(int(f.readline())):
    list_cities = f.readline().split()
    dct_cities[list_cities[0]] = set(list_cities[1:])

for i in range(int(f.readline())):
    city = f.readline().strip()
    for country, cities in dct_cities.items():
        if city in cities:
            print(country)
            break

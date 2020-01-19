"""
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
"""
country_count = int(input("Please enter the number of countries:"))
country_cities = {}
for country_index in range(country_count):
    country_str = input("Please describe the " + str(country_index+1) + " country:")
    lst1 = country_str.split()
    country_cities[lst1[0]] = lst1[1:]
cities_count = int(input("Please enter the number of cities:"))
lst_cities = []
for index_cities in range(cities_count):
    lst_cities.append(input("Please enter the" + str(index_cities+1) + " city"))
for city in lst_cities:
    print(list(country for (country, cities) in country_cities.items() if city in cities)[0])

# 2. Города
# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.

dct = {}
for the_list in range(int(input("Enter the number of lists: "))):
    country, *cities = input("Enter a list: ").split()
    dct[country] = cities
for city in range(int(input("Enter the number of cities: "))):
    the_city = input("Enter the city: ")
    count = 0
    for country, cities in dct.items():
        if the_city in cities:
            print(country)
            count += 1
    if count == 0:
        print("There is no such city in the database")

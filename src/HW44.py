# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
countries = {}
count_countries = int(input("Enter count of countries: "))
for _ in range(count_countries):
    country, *cities = input("Enter country and cities: ").split()
    countries[country] = cities
count_cities = int(input("Enter count of cities: "))
for _ in range(count_cities):
    city = input("Enter city: ")
    for country, cities in countries.items():
        if city in cities:
            print(country)

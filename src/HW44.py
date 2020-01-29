# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
countries = {}
for i in range(int(input("Введите количество стран: "))):
    country, *cities = input("Введите список стран и городов: ").split()
    for city in cities:
        countries[city] = country
print("Введите количество городов: ")
for i in countries:
    print(countries.get(input("Введите город: "),
                        "Такого города нет в списке"))

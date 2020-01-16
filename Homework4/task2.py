# 2. Города
# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.

dct = {}
for i in range(int(input("Enter the number of lists: "))):
    country, *cities = input("Enter a list: ").split()
    for city in cities:
        dct[city] = country

for i in range(int(input("Enter the number of cities: "))):
    print(dct.get(input("Enter a city: "),
                  "There is no such city in the database"))

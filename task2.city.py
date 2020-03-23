# Дан список стран и городов каждой страны.
# Затем даны названия городов. Для каждого
# города укажите, в какой стране он находится.
#
# исходные данные:
# 3
# Russia Moscow Petersburg Novgorod Kaluga
# Ukraine Kiev Donetsk Odessa
# Belarus Brest
# 3
# Odessa
# Brest
# Novgorod
# #########
# Создаем словарь с ключом - страна, значение - города(список),
# получаем список городов для проверки, пробегаемся по нему,
# сверяем значение словаря со списком для проверки, если
# находим печатаем ключ.
my_dict = {}
for i in range(int(input())):
	country, *city = input().split()
	my_dict[country] = city  # создаем словарь
list_check = []
for j in range(int(input())):
	city = input()
	list_check.append(city)  # создаем список для проверки
for u in list_check:
	for key, value in my_dict.items():
		if u in value:
			print(key)

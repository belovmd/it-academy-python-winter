# Дан список. Выведите те его элементы, которые встречаются в списке
# только один раз. Элементы нужно выводить в том порядке, в котором
# они встречаются в списке.

lst = list(input('Введите список: '))
count_elements = {}

for element in lst:
    count_elements[element] = count_elements.get(element, 0) + 1

result = [element for element in lst if count_elements[element] == 1]
print(result)

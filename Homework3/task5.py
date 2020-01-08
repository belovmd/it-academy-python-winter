# 5. Уникальные элементы в списке
# Дан список.
# Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

lst = [int(num) for num in input('Enter string of numbers: ').split()]
result_list = []
for elem in lst:
    if lst.count(elem) == 1:
        result_list.append(elem)
for num in result_list:
    print(num, end=' ')

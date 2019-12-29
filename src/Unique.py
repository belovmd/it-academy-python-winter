"""
Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются в списке только один
раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""

lst_1 = [int(el) for el in input().split()]
dct_1 = {}
for el in lst_1:
    if dct_1.get(el) is None:
        dct_1[el] = 0
    dct_1[el] += 1
print(dct_1)
for el in dct_1.keys():
    if dct_1.get(el) == 1:
        print(el, end=" ")

# через count
print("\n")
for el in lst_1:
    if lst_1.count(el) == 1:
        print(el, end=" ")
